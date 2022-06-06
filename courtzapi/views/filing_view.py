from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from courtzapi.models import Filing
from courtzapi.models.case_status import CaseStatus
from courtzapi.models.dockets import Docket
from courtzapi.models.filers import Filer
from courtzapi.models.filing_type import FilingType
from courtzapi.serializers import FilingSerializer

class FilingView(ViewSet):
    def list(self, request):
        """ GET list of filings """
        return ""
    
    def retrieve(self, request, pk):
        """GET single filing"""
        filing = Filing.objects.get(pk=pk)
        serializer = FilingSerializer(filing)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """ POST single filing """
        # data needed in request
        # filer comes from the request token
        # docket_index generated from length of docket
        # in body of request
            # docket_id - if blank, make new docket
            # filing_type_id
            # file_url
        
        new_docket = not request.data["docket_id"]
        
        # needs to check if the filing is a new docket
        if new_docket:
            # get case_num of last docket
            # status = open (1)
            # last_docket_case_num = Docket.objects.last().case_num
            new_status = CaseStatus.objects.get(pk=1)
            created_docket = Docket.objects.create(
                case_num = "testString",
                status=new_status,
            )
            docket = Docket.objects.last()
        
        # or if the filing should create a docket as well
        else:
            docket = Docket.objects.get(pk=request.data["docket_id"])
        
        filer = Filer.objects.get(pk=request.auth.user.id)
        filing_type= FilingType.objects.get(pk=request.data['filing_type_id'])
        docket_index = len(docket.filings.all()) + 1
        judge_req = False
        is_judge = False
        
        if filing_type.id == 2:
            judge_req = True
            is_judge = filer.filer_type_id == 2
        
        if judge_req and not is_judge:
            return Response({'message': "Only judges can make orders"}, status=status.HTTP_401_UNAUTHORIZED)   

        new_filing = Filing.objects.create(
            filer=filer,
            docket=docket,
            docket_index=docket_index,
            filing_type=filing_type,
            title=request.data['title'],
            file_url = request.data['file_url']
        )
        serializer = FilingSerializer(new_filing)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        """ DELETE single filing """
        return ""

    # currently not allowing filing updates
    # misfiled items should be amended using a new filing    
    # def update(self):
    #     return ""