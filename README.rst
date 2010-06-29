cmsplugin-banner
===

the default settings are: 

the (css) class choices
CMSPLUGIN_BANNER_STYLE_CHOICES = ( ('default','default'), )

add `"cmsplugin_banner.context_processors.plugin_ad_slots"` to `TEMPLATE_CONTEXT_PROCESSORS`

Setup for Google Ads:
* load googles javascript somewhere: `<script type="text/javascript" src="http://partner.googleadservices.com/gampad/google_service.js"></script>`
* initialize the slots somewhere in `<head>` by including `cmsplugin_banner/header_include.html`. This assumes you also add
`<script type="text/javascript">GA_googleFetchAds();</script>` to head and have a context variable called `AD_ACCOUNT_IDENTIFIER` with the google ad account id.