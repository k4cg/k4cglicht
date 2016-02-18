from beautifulhue.api import Bridge

class BridgeWrapper(object):

    def __init__(self, config):
        self.bridge = self.__createBridge(config)

    def __createBridge(self, config):
        bridge = Bridge(device={'ip': config['bridgeip']}, user={
                        'name': config['username']})

        resource = {'which': 'system'}
        response = bridge.config.get(resource)['resource']
        if 'lights' in response:  # user is authorized
            return bridge
        elif 'error' in response[0]:  # user is not authorized
            error = response[0]['error']
            if error['type'] == 1:
                self.__createConfig(bridge, config)

        return bridge

    def __createConfig(self, bridge, config):
        created = False
        print('Press the button on the Hue bridge')
        while not created:
            resource = {'user': {'devicetype': config[
                'devicetype'], 'name': config['username']}}
            response = bridge.config.create(resource)['resource']
            if 'error' in response[0]:
                if response[0]['error']['type'] != 101:
                    print('Unhandled error creating configuration on the Hue')
                    sys.exit(response)
                else:
                    created = True

    def __update(self, to_update, resource):
        to_update.update(resource)

    def set_group_brightness(self, brightness):
        resource = {'which':1, 'data':{'action':{'bri':brightness}}}
        self.__update(self.bridge.group, resource)

    def set_group(self, xy, transition=1, brightness=254):
        resource = {'which':1, 'data':{'action':{'bri':brightness,'xy':xy,'transitiontime':transition}}}
        self.__update(self.bridge.group, resource)
