import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from scapy.all import ARP, Ether, srp

from .models import Device

class DeviceDetectionConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def detect_devices(self, event):
        self.send(text_data=json.dumps(event))

    def scan_network(self):
        known_devices = Device.objects.all()
        connected_devices = []

        # Send ARP broadcast request to detect devices on the network
        arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst="10.0.2.0/24")
        result = srp(arp_request, timeout=3, verbose=0)[0]

        for sent, received in result:
            mac_address = received.hwsrc
            if mac_address != self.scope['headers'][2][1].decode():
                connected_devices.append(mac_address)

        for device in known_devices:
            if device.mac_address not in connected_devices:
                self.send(text_data=json.dumps({
                    'type': 'device_connected',
                    'device_name': device.name,
                    'device_mac_address': device.mac_address,
                }))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        command = text_data_json['command']

        if command == 'start_detection':
            async_to_sync(self.channel_layer.group_add)('device_detection', self.channel_name)
            self.scan_network()

        elif command == 'stop_detection':
            async_to_sync(self.channel_layer.group_discard)('device_detection', self.channel_name)
