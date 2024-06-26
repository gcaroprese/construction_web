import re


class MobileDetectionMiddleware(object):
    """
    Useful middleware to detect if the user is
    on a mobile device.
    """

    def process_request(self, request):
        is_mobile = False
        is_tablet = False

        if request.META.has_key('HTTP_USER_AGENT'):
            user_agent = request.META['HTTP_USER_AGENT']

            tablet_pattern = "(ipad|android|android 3.0|xoom|sch-i800|playbook|tablet|kindle)"
            tablet_match = re.compile(tablet_pattern, re.IGNORECASE).search(user_agent)

            mobile_pattern = "(blackberry|iphone|android|mmp|symbian|smartphone|midp|wap|phone|windows ce|pda|mobile|mini|palm|netfront)"
            mobile_match = re.compile(mobile_pattern, re.IGNORECASE).search(user_agent)

            if mobile_match:
                is_mobile = True
            elif tablet_match:
                is_tablet = True
            else:
                if request.META.has_key('HTTP_ACCEPT'):
                    http_accept = request.META['HTTP_ACCEPT']

                    wap_pattern = "application/vnd\.wap\.xhtml\+xml"
                    wap_match = re.compile(wap_pattern, re.IGNORECASE).search(http_accept)

                    if wap_match:
                        is_mobile = True

                if not is_mobile: # Test user_agent against a biggger list.
                    user_agents_test = ("w3c ", "acs-", "alav", "alca", "amoi", "audi",
                                        "avan", "benq", "bird", "blac", "blaz", "brew",
                                        "cell", "cldc", "cmd-", "dang", "doco", "eric",
                                        "hipt", "inno", "ipaq", "java", "jigs", "kddi",
                                        "keji", "leno", "lg-c", "lg-d", "lg-g", "lge-",
                                        "maui", "maxo", "midp", "mits", "mmef", "mobi",
                                        "mot-", "moto", "mwbp", "nec-", "newt", "noki",
                                        "xda",  "palm", "pana", "pant", "phil", "play",
                                        "port", "prox", "qwap", "sage", "sams", "sany",
                                        "sch-", "sec-", "send", "seri", "sgh-", "shar",
                                        "sie-", "siem", "smal", "smar", "sony", "sph-",
                                        "symb", "t-mo", "teli", "tim-", "tosh", "tsm-",
                                        "upg1", "upsi", "vk-v", "voda", "wap-", "wapa",
                                        "wapi", "wapp", "wapr", "webc", "winw", "winw",
                                        "xda-")

                    test = user_agent[0:4].lower()
                    if test in user_agents_test:
                        is_mobile = True

        request.is_mobile = is_mobile
        request.is_tablet = is_tablet