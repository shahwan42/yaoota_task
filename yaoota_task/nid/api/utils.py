from django.utils import timezone
from rest_framework.exceptions import ValidationError


max_days_in_each_month = {
    "01": "31",
    "02": "29",
    "03": "31",
    "04": "30",
    "05": "31",
    "06": "30",
    "07": "31",
    "08": "31",
    "09": "30",
    "10": "31",
    "11": "30",
    "12": "31",
}
governorates = {
    "01": "Cairo",
    "02": "Alexandria",
    "03": "Port Said",
    "04": "Suez",
    "11": "Damietta",
    "12": "Dakahlia",
    "13": "Sharqia",
    "14": "Qalyubia",
    "15": "Kafr El Sheikh",
    "16": "Gharbia",
    "17": "Monufia",
    "18": "Beheira",
    "19": "Ismailia",
    "21": "Giza",
    "22": "Beni Suef",
    "23": "Faiyum",
    "24": "Minya",
    "25": "Asyut",
    "26": "Sohag",
    "27": "Qena",
    "28": "Aswan",
    "29": "Luxor",
    "31": "Red Sea",
    "32": "New Valley",
    "33": "Matruh",
    "34": "North Sinai",
    "35": "South Sinai",
    "88": "Abroad",
}


def extract_id_data(id_number: str):
    return {
        "millennium": id_number[0],
        "year": id_number[1:3],
        "month": id_number[3:5],
        "day": id_number[5:7],
        "birth_governorate": id_number[7:9],
        "serial": id_number[9:13],
        "gender": id_number[12],
        "checksum": id_number[13],
    }


def validate_id_data(id_data: dict):
    # validate millennium
    millennium = id_data.get("millennium")

    if millennium not in ["2", "3"]:
        raise ValidationError("Invalid")

    # validate year
    year = id_data.get("year")

    # 1900 - 1999 with millennium = 2
    if millennium == "2" and not (0 <= int(year) <= 99):
        raise ValidationError("Invalid")

    # 2000 - now with millennium = 3
    if millennium == "3" and not (0 <= int(year) <= int(str(timezone.now().year)[2:])):
        raise ValidationError("Invalid")

    # validate month
    month = id_data.get("month")
    if not (1 <= int(month) <= 12):
        raise ValidationError("Invalid")

    # validate days
    day = id_data.get("day")
    if not (1 <= int(day) <= int(max_days_in_each_month[month])):
        raise ValidationError("Invalid")
    # NOTE we could go further and calculate leap years
    # and validate Feb days if year is leap or not

    # validate governorates
    birth_governorate = id_data.get("birth_governorate")
    if birth_governorate not in governorates.keys():
        raise ValidationError("Invalid")

    # validate serial

    # validate gender
    gender = id_data.get("gender")
    if int(gender) not in range(1, 10):
        raise ValidationError("Invalid")

    # validate checksum
    checksum = id_data.get("checksum")
    if int(checksum) not in range(1, 10):
        raise ValidationError("Invalid")
