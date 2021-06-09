from flask import Flask
from flask import request

app = Flask(__name__)

testa = "no"

@app.route('/Haro')
def hello_world():
   return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/JoshSWProject', methods=['POST'])
def adaptiveCardReceiver():
   testa1 = request.get_json()
   print(testa1)
   testa = "yes"
   return "%s" % testa

def changeTesta() :
   testa = "no"

@app.route('/ToSecureX', methods=['POST'])
def webexSender():
   toRemediate = testa
   changeTesta()
   if(toRemediate == "yes") :
      return "%s" % "yes"
   else:
      return "%s" % "no"

@app.route('/Hi')
def hi_world():
   return testa

if __name__ == '__main__':
   app.run()



