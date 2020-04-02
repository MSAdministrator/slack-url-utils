import pendulum
import yaml
from OTXv2 import OTXv2


class OTXPulse(object):

    _submission_time = pendulum.now().add(hours=8)
    _API_KEY = None # '435cc70edbfcfb58a0bd29bb900378ee3b8a8d2aa1e8a3ec254e572fe55d9d82'

    def __init__(self):
        self._API_KEY = self.__load_config()
        self.otx = OTXv2(self._API_KEY)

    def __load_config(self):
        with open('./config.yml', 'r') as stream:
            try:
                return yaml.safe_load(stream)['otx_token']
            except yaml.YAMLError as exc:
                print(exc)

    def new(self, indicator, type):
        pass
        #indicators = {}
        #indicators['type'] = type
        #indicators['indicator'] = indicator
        #response = otx.create_pulse(name='Submitted ')

    def new_via_slack(self, slack_obj):
        response_string = ''
        indicators = []
        name = 'Submitted by {name} in {channel} in {domain} Slack'.format(
            name=slack_obj['user_name'],
            channel=slack_obj['channel_name'],
            domain=slack_obj['team_domain']
            )
        text = slack_obj['text'].split()
        if len(text) == 2:
            indicators.append({
                'indicator': text[1],
                'type': text[0]
            })
        response = self.otx.create_pulse(name=name ,public=True ,indicators=indicators ,tags=[] , references=[])
        if 'pulse_name' in response:
            response_string += '{pulse} created via {author} with id of {id}.\n\n'.format(
                pulse=response['pulse_name'],
                author=response['author_name'],
                id=response['id'],
            )
            if 'indicators' in response:
                if response['indicators']:
                    for item in response['indicators']:
                        response_string += 'The *{indicator}* of type *{type}* was added and will expire on {expiration}.'.format(
                            indicator=item['indicator'],
                            type=item['type'],
                            expiration=item['expiration']
                        )
        if response_string is not '':
            return response_string
        else:
            return 'Unable to sumbit Indicator to OTX'