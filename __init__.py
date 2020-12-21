from mycroft import MycroftSkill, intent_file_handler


class MorningWakingUp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('up.waking.morning.intent')
    def handle_up_waking_morning(self, message):
        self.speak_dialog('up.waking.morning')


def create_skill():
    return MorningWakingUp()

