import arrow
import sys
sys.dont_write_bytecode = True

# TODO change all utc vals to lm
def single_date_hour(lm):
    local = utc_builder(lm)
    local.format('YYYY-MM-DD-HH').replace("+", "%2B")
    local = str(local)[:-19].replace("T", "-")
    # print "locolocal date: %s" %local
    return local

def month_date(lm):
    local = utc_builder(lm)
    local.format('YYYY-MM-DD-HH').replace("+","%2B")
    span_local = local.span('month')
    spandateEnd = str(span_local[1]).format('YYYY-MM-DD').replace("+", "%2B").replace("9.99999", "")
    local = str(spandateEnd) # [:-22]
    monthdate = "?date=%s" % local
    # print monthdate
    return monthdate

def daterange_date(lm):
    local = utc_builder(lm)
    local.format('YYYY-MM-DD-HH').replace("+", "%2B")
    span_local = local.span('hour')

    spandateStart = str(span_local[0]).format('YYYY-MM-DD-HH').replace("+", "%2B")
    spandateEnd = str(span_local[1]).format('YYYY-MM-DD-HH').replace("+", "%2B").replace("9.99999", "")
    daterange =  "start=%s&end=%s" % (spandateStart, spandateEnd)
    # print daterange
    return daterange

def span_date(lm):
    local = utc_builder(lm)
    local.format('YYYY-MM-DD-HH').replace("+", "%2B")
    span_local = local.span('month')

    spandateStart = str(span_local[0]).format('YYYY-MM-DD-HH').replace("+", "%2B")
    spandateEnd = str(span_local[1]).format('YYYY-MM-DD-HH').replace("+", "%2B").replace("9.99999", "")
    daterange =  "start=%s&end=%s" % (spandateStart, spandateEnd)
    spanlist = [spandateStart, spandateEnd]
    # print spanlist
    return spanlist

def end_date(lm):
    local = utc_builder(lm)
    local.format('YYYY-MM-DD-HH').replace("+", "%2B")
    span_local = local.span('month')
    spandateEnd = str(span_local[1]).format('YYYY-MM-DD-HH').replace("+", "%2B").replace("9.99999", "")
    local = str(local)[:-22]
    # print spandateEnd
    return spandateEnd[:-8]

def single_end_date_hours(lm):
    local = utc_builder(lm)
    local.format('YYYY-MM-DD-HH').replace("+", "%2B")
    span_local = local.span('month')
    spandateend = str(span_local[1]).format('YYYY-MM-DD-HH').replace("+", "%2B").replace("9.99999", "")
    local = str(local)[:-22]
    # print spandateend
    return spandateend

def single_end_date(lm):
    local = utc_builder(lm)
    local.format('YYYY-MM-DD').replace("+", "%2B")
    span_local = local.span('month')
    spandateend = str(span_local[1]).format('YYYY-MM-DD').replace("+", "%2B").replace("9.99999", "")
    local = str(local)[:-22]
    return spandateend

def utc_builder(lm):
    if lm == "now":
        utc = arrow.utcnow().to('GMT')
    else:
        utc = arrow.utcnow().replace(months=-lm - 1).to('GMT')
    return utc

def mo_year(lm):
    local = utc_builder(lm)
    return local.format('MMM_YY')



# TODO example arrow usage
# sdate = "2014-01-01-19"
# edate = "2014-01-31-20"
# # print "sdate: " + sdate
# # print "edate: " + edate
# sdatep = str(arrow.get(sdate, 'YYYY-MM-DD-HH')).replace("+","%2B")
# edatep = str(arrow.get(edate, 'YYYY-MM-DD-HH')).replace("+","%2B")
# sdatep = arrow.get(sdate, 'YYYY-MM-DD-HH').isoformat(sep='T')
# edatep = arrow.get(edate, 'YYYY-MM-DD-HH').isoformat(sep='T')
# print "sdatep: " + str(sdatep)
# print "edatep: " + str(edatep)
