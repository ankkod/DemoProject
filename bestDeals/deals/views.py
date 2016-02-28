from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponse
import deals
from deals.models import Category





def submit(request):
    return render_to_response("submitpage.html")

def submitdeal(request):
    dealurl=request.GET.get("dealurl",None)
    dealtitle=request.GET.get("dealtitle",None)
    dealprice=request.GET.get("dealprice",None)
    dealdetails=request.GET.get("dealdetails",None)
    dealuploadimage=request.GET.get("dealuploadimage",None)
    dealimageurl=request.GET.get("dealimageurl",None)
    dealimagetags=request.GET.get("dealtags",None)
    dealstartdate=request.GET.get("dealstartdate",None)
    dealenddate=request.GET.get("dealenddate",None)
    dealresult=deals.models.Deal(deal_id=001,deal_url=dealurl,image=dealuploadimage,title=dealtitle,price=dealprice,tags=dealimagetags,startdate=dealstartdate,enddate=dealenddate)
    dealresult.save()
    
    return render_to_response('check.html')

def submitvouchers(request):
    voucherurl=request.GET.get("voucherurl",None)
    vouchertitle=request.GET.get("vouchertitle",None)
    vouchertopic=request.GET.get("vouchertopic",None)
    voucherdiscount=request.GET.get("voucherdiscount",None)
    vouchercode=request.GET.get("vouchercode",None)
    vouchertags=request.GET.get("vouchertags",None)
    voucherminspend=request.GET.get("voucherminspend",None)
    voucherappliesto=request.GET.get("voucherappliesto",None)
    voucherstartdate=request.GET.get("voucherstartdate",None)
    voucherenddate=request.GET.get("voucherenddate",None)
    categoryresult=deals.models.Category(category_id=vouchertopic,category_name=voucherappliesto)
    categoryresult.save()
    
    voucherresult=deals.models.Voucher(voucher_id=002,deal_url=voucherurl,discount=voucherdiscount,code=vouchercode,minimum_spend=voucherminspend,title=vouchertitle,category_id=vouchertopic,tags=vouchertags,startdate=voucherstartdate,enddate=voucherenddate)
    voucherresult.save()
   
    
    return render_to_response('check.html')
         
def submitfreebie(request):
    freebieurl=request.GET.get("freebieurl",None)
    freebietitle=request.GET.get("freebietitle",None)
    freebiedetails=request.GET.get("freebiedetails",None)
    freebieuploadimage=request.GET.get("freebieuploadimage",None)
    freebieimageurl=request.GET.get("freebieimageurl",None)
    freebietags=request.GET.get("freebietags",None)
    freebiestartdate=request.GET.get("freebiestartdate",None)
    freebieenddate=request.GET.get("freebieenddate",None)
    freebieresult=deals.models.Freebies(freebies_id=001,deal_url=freebieurl,details=freebiedetails,image=freebieuploadimage,title=freebietitle,tags=freebietags,startdate=freebiestartdate,enddate=freebieenddate)
    freebieresult.save()
    
    return render_to_response('check.html')
       
       
def submitask(request):         
    askquestion=request.GET.get("askquestion",None)
    asktags=request.GET.get("asktopic",None)
    askdetails=request.GET.get("askdetails",None)
    
    askresult=deals.models.Ask(ask_id=001,question=askquestion,details=askdetails,tags=asktags)
    askresult.save()
    
    return render_to_response('check.html')
   