# Written by Nikhil Alapati
# This program Is a sample usage for the GrammarChecker class

# imports the GrammarChecker functions
import GrammarChecker as G
# imports time
import time
from selenium import webdriver
driver = webdriver.PhantomJS()
# timeouts if grammarly takes mre than 10 seconds for the sake of server
driver.set_page_load_timeout("10")
# instrcts chrome to go to the signin page
driver.get("https://www.grammarly.com/signin?allowUtmParams=true")
# calls the function to log in
G.login(driver, "y555417@nwytg.net", "password")
time.sleep(7)
# calls the check document function here is a sample crappy essay written by me in 8th or 9th grade
G.CheckDocument(driver, """Dear Thomas,
	Hey, Thomas I’m an anonymous guy. also, I’m your well wisher. I’m going to talk to you about the strengths and weaknesses. The things I like about you  is that you are getting used to the glade really fast I mean faster than a normal person would and you were making good decisions most of the time and you were intelligent and brave I’m saying this because if I wake up in a place that I don't know I would be crying and scared  but you aren’t scared and you got used to the people really fast. You are preventing to not make a lot of enemies by fighting with them or any other way, and when Minho and Alby won’t make it before the door closes you were so brave and rushed to help and save their lives. Although you have a lot of strengths you also have a lot of weaknesses the first one is that you had a loss of memory not like others that remember things. Because of loss of memory you can’t remember how you got there and who is your family what country you live in. At the starting of the story,  you were scared that you are going to die and loose in your confidence, and you are not able to concentrate on things sometimes . Some of the bad choices that you have made is that while the Griever chasing you, you did a rope swing like Tarzan you are not Tarzan you could have broken your butt and your teeth, but I really liked your bravery.
Your friendly
Anonymous. 



The Maze Runner
by James Dashner 
Letter by Nikhil Alapati
""")
G.PostUrlCookies(driver)
