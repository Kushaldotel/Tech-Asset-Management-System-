# from .models import Organization_Details
# from django.utils.translation import gettext as _

# from django.urls import reverse
# from django.utils.html import format_html


# def my_custom_element():
#     return {
#         'title': 'My Custom Element',
#         'content': 'This is my custom element content.',
#         'template': '',
#         'order': 1
#     }


JAZZMIN_SETTINGS = {
    # title of the window (Will default to current_admin_site.site_title if absent or None)
    "site_title": "Trilokya Admin",
    "site_brand": "Trilokya Technology",
    # # "site_brand": Organization_Details._meta.get_field('name'),

    # # Title on the login screen (19 chars max) (defaults to current_admin_site.site_header if absent or None)
    "site_header": "Trilokya Admin",
    "welcome_sign": "Welcome to Trilokya",
    "copyright": "Trilokya Technology",
    "site_logo": "tri.png",
    # "language_chooser": True,

    
        # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "Support", "url": "https://www.linkedin.com/company/trilokya-technology/", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        {"model": "blog.Service"},
        #make search field
        
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "blog"},
        
    ],
    
    #Command to hide the specific model you need
    # "hide_models":["blog.Vendor",], 

#Customizing icons:
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        # "blog.Service": "fas fa-tachometer-alt",
        # the fa-tachometer-alt displays dashboard
        
        
        "blog.Branchstatus": "fas fa-code-branch",
        "blog.Branch": "fas fa-code-branch",
        "blog.Country": "fas fa-globe",
        "blog.Criticality": "fas fa-exclamation-triangle",
        "blog.ManagedBy": "fas fa-building",
        "blog.Documentcategory": "fas fa-file-alt",
        "blog.Document": "fas fa-file-alt",
        "blog.Hardwaretype": "fas fa-microchip",
        "blog.Hardware": "fas fa-desktop",
        "blog.Insurance": "fas fa-shield-alt",
        "blog.Organization_Details": "fas fa-building",
        "blog.Service": "fas fa-cogs",
        "blog.Softwaretype": "fas fa-cube",
        "blog.Software": "fas fa-cube",
        "blog.State": "fas fa-map-marker-alt",
        #pulse will add animation
        # "blog.Status": "fas fa-check-circle fa-pulse",
        "blog.Status": "fas fa-check-circle",
        "blog.Vendor": "fas fa-truck",
        
        
    },
    

    
    
    "site_icon": "tri.png",
    # <i class="fa-solid fa-gauge-high"></i>
    
    
# "language_chooser": True,
# "custom_links": {
#     "books": [{
#         # Any Name you like
#         "name": "Make Messages",

#         # url name e.g `admin:index`, relative urls e.g `/admin/index` or absolute urls e.g `https://domain.com/admin/index`
#         "url": "make_messages",

#         # any font-awesome icon, see list here https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2 (optional)
#         "icon": "fas fa-comments",

#         # a list of permissions the user must have to see this link (optional)
#         "permissions": ["books.view_book"]     
#     }]
# },
# "changeform_format": "horizontal_tabs",
# override change forms on a per modeladmin basis
# "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},

# 'custom_css': 'blog/css/custom.css'
}

# JAZZMIN_DASHBOARD_ADMIN_ORDER = [    my_custom_element,    ...]
