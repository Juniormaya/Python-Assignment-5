class socialmedia:
    def open(self):
        print("Open social media app")

class instagram(socialmedia):
    def open(self):
        print("Open Instagram app")

class facebook(socialmedia):    
    def open(self):
        print("Open Facebook app")  

class twitter(socialmedia):
    def open(self):
        print("Open Twitter app")

class tiktok(socialmedia):
    def open(self):
        print("Open TikTok app")

# Example usage
for app in [instagram(), facebook(), twitter(), tiktok()]:
    print(app.open())