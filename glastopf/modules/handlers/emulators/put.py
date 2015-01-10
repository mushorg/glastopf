from glastopf.modules.handlers import base_emulator


class PUTRequest(base_emulator.BaseEmulator):
  
  def __init__(self, data_dir):
    
    super(PUTRequest, self).__init__(data_dir)
    
  def handle(self, attack_event):
    attack_event.set_response('', http_code=200)
