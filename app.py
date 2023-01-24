from DataCalculatorPackage import data_calculator_class
from ImageChangerPackage import image_changer_class
from InstagramStoryPosterPackage import instagram_story_poster_class

class App:
    def run():
        days_number = data_calculator_class.data_calculator()
        image_changer_class.image_changer(days_number)
        instagram_story_poster_class.instagram_story_poster()

if __name__ == '__main__':
    App.run()