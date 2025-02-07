# Ines

from abc import ABCMeta, abstractmethod


class IContent:
    __metaclass__ = ABCMeta

    @staticmethod
    @abstractmethod
    def format_text(content):
        pass


class MyContent(IContent):
    def __init__(self, text):
        self.text = self.format_text(text)

    @staticmethod
    def format_text(text):
        return '\n'.join(['<myML>', text, '<myML>'])


class HTMLContent(IContent):
    def __init__(self, text):
        self.text = self.format_text(text)

    @staticmethod
    def format_text(text):
        return '\n'.join(['<div>', text, '</div>'])


class IEmail(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, contend):
        pass


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == 'IM':
            self.__sender = ''.join(["I'm ", sender])
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == 'IM':
            self.__receiver = ''.join(["I'm ", receiver])
        else:
            self.__receiver = receiver

    def set_content(self, contend):
        self.__content = contend.text

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"

        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)


email = Email('IM')
email.set_sender('qmal')
email.set_receiver('james')
content = HTMLContent('Hello, there!')
email.set_content(content)
print(email)
