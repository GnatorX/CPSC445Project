from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def getPicture(sequence):
    brower=webdriver.Firefox()
    browser.get("http://mr-nutz.no-ip.org/rnastrat/?p=tools&p2=renderalign")
    elem = browser.find_element_by_name("aligned_ss_text")
    elem.send_keys(sequence)
    brower.find_element_by_type("submit").click()

getPicture(">Unnamed Query Structure\nACCUGGUGUGAAUUGCAGAAUCCCGUGAACCAUCGAGU\n((.(((((((.(((....))).).).....))))).))\n>Unnamed Structure\nGC-CCG-AGG-C-CAUCCG-G-C-C-GA-----GG-GC\n((-((.-.((-(-(....)-)-)-)-..-----))-))\n#>SCENARIO\nSMdhSADaSMdSDSssssSDSdMdSdmmddaDASHdMS")
