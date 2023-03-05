from datetime import date
def handle_date(date_from_req: str):
    day, month, year = date_from_req.split("/")    
    return date(int(year), int(month), int(day))