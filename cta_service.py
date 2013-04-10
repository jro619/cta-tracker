from bottle import route, run, SimpleTemplate, template
from source import CTASource
from client import CTAClient
import logger

logger.initialize()

cta_source = CTASource()
client = CTAClient(cta_source)

@route('/')
def run_app():
  now_time = client.get_current_time()
  current_time = now_time.strftime('%I:%M:%S %p')
  return template('base.tpl',
      stations=client.stations,
      trains=client.trains,
      current_time=current_time)

def shutdown():
  server.socket.close()
        
def main():
  try:
    run(host='0.0.0.0', port=8000, debug=True)
  except KeyboardInterrupt:
    logger.info('^C Received. Shutting Down Server.')
    shutdown()
  except:
    logger.error('Unknown Exception occurred')
    shutdown()
    
if __name__ == '__main__':
  main()
