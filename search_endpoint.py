from juriscraper.pacer.http import PacerSession
from juriscraper.pacer.hidden_api import PossibleCaseNumberApi

pacer_sess = PacerSession(username="", password="")

court_id = "dcd"
docket_id = "9000013"
office_id ="1"
docket_param = "cv"

#court_id = "nmi"
#docket_id = "8800001"

api = PossibleCaseNumberApi(court_id=court_id,pacer_session=pacer_sess)

resp = api.query(docket_id)

print resp
print api.data(office_number=office_id, docket_number_letters=docket_param)

#resp = api.query("7801294")
#print res
