# config/settings/unfold_settings.py

from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static

UNFOLD = {
    "SITE_TITLE": "ASADMAXMUD",
    "SITE_HEADER": "ASADMAXMUD",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("logo/logo.png"),  # Light mode logo
        "dark": lambda request: static("logo/logo.png"),   # Dark mode logo
    },
    "SITE_LOGO": {
        "light": lambda request: static("logo/logo.png"),  # Light mode logo
        "dark": lambda request: static("logo/logo.png"),   # Dark mode logo
    },
    "SITE_SYMBOL": "speed",  # Symbol from the icon set
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/png",  # Updated to PNG for better compatibility
            "href": lambda request: static("logo/favicon.png"),
        },
    ],
    "SHOW_HISTORY": True,  # Show/hide the "History" button
    "SHOW_VIEW_ON_SITE": True,  # Show/hide the "View on site" button
    "ENVIRONMENT": None,
    "DASHBOARD_CALLBACK": None,
    "STYLES": [
        lambda request: static("css/style.css"),  # Custom styles
    ],
    "SCRIPTS": [
        lambda request: static("js/script.js"),  # Custom scripts
    ],
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "fr": "🇫🇷",
                "nl": "🇧🇪",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,  # Enable search in applications and models names
        "show_all_applications": True,  # Dropdown with all applications and models
        "navigation": [
            {
                "title": _("Asosiy Sahifa"),
                "separator": False,  # Top border
                "collapsible": True,
                "items": [
                    {
                        "title": _("Asosiy sahifa"),
                        "icon": "home",
                        "link": reverse_lazy("admin:index"),
                    },
                    {
                        "title": _("Foydalanuvchilar"),
                        "icon": "person",
                        "link": reverse_lazy("admin:users_usermodel_changelist"),
                    },
                ],
            },
            {
                "title": _("Mahsulot va Kategoryalar"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Mahsulotlar"),
                        "icon": "inventory", 
                        "link": reverse_lazy("admin:product_productmodel_changelist"),
                    },
                    {
                        "title": _("Kategoryalar"),
                        "icon": "category",  
                        "link": reverse_lazy("admin:product_categorymodel_changelist"),
                    },
                    {
                        "title": _("Bannerlar"),
                        "icon": "image", 
                        "link": reverse_lazy("admin:product_bannermodel_changelist"),
                    },
                ],
            },
            {
                "title": _("Qo'shimcha Elementlar"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Mahsulot rangi"),
                        "icon": "palette",  # Django Unfold ikonkasi
                        "link": reverse_lazy("admin:product_colormodel_changelist"),
                    },
                    {
                        "title": _("Mahsulot o'lchami"),
                        "icon": "straighten",  # Django Unfold ikonkasi
                        "link": reverse_lazy("admin:product_sizemodel_changelist"),
                    },
                    {
                        "title": _("Reklama"),
                        "icon": "campaign",  
                        "link": reverse_lazy("admin:bot_advertisingmodel_changelist"),
                    },
                ],
            },
            {
                "title": _("Savat va Buyurtmalar"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Savatcha"),
                        "icon": "shopping_cart",  # Django Unfold ikonkasi
                        "link": reverse_lazy("admin:basket_cartmodel_changelist"),
                    },
                    {
                        "title": _("Savat Buyumlar"),
                        "icon": "shopping_cart",  # Django Unfold ikonkasi
                        "link": reverse_lazy("admin:basket_cartitemmodel_changelist"),
                    },
                    {
                        "title": _("Buyurtmalar"),
                        "icon": "receipt_long",  # Django Unfold ikonkasi
                        "link": reverse_lazy("admin:order_ordermodel_changelist"),
                    },
                ],
            },
            {
                "title": _("Telegram Bot"),
                "separator": True,
                "collapsible": True,
                "items": [
                    {
                        "title": _("Bot haqida malumot"),
                        "icon": "info",  # Django Unfold ikonkasi
                        "link": reverse_lazy("admin:bot_aboutmodel_changelist"),
                    },
                ],
            },
        ],
    },
}
