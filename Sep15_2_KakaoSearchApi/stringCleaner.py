# -*- coding:utf-8 -*-

class StringCleaner:
    
    @staticmethod
    def clean(s):
        s = s.replace("&quot;", " ").replace("&apos;", "").replace("<b>","").replace("</b>", "")
        
        return s
    
    