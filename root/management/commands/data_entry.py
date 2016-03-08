from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction, IntegrityError
import xlrd
import glob
from root.models import *

class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        import pdb;pdb.set_trace()
        #for file_name in glob.glob("states/*.xls"):
        # book = open_workbook('forum.xlsx')
        # sheet = book.sheet_by_index(3)

        # read header values into the list    
        # keys = [sheet.cell(0, col_index).value for col_index in xrange(sheet.ncols)]
        import pdb;pdb.set_trace()
        book = xlrd.open_workbook("pincode.xlsx", on_demand = True)
        sheet = book.sheet_by_index(0)
        number_of_lines = sheet.nrows
        report_header_list = []
        for header in sheet.row_values(0):
            report_header_list.append(header.lower().replace(' ','_'))
        try:
            for row in range(1, number_of_lines):
                row_list = sheet.row_values(row)
                row_dict = dict(zip(report_header_list, row_list))
                if row_dict['officename'].strip():
                    village_name = row_dict['officename'].replace('B.O', '').replace('S.O', '')
                    state_name = row_dict['statename']
                    pincode = row_dict['pincode']
                    district = row_dict['districtname']
                    taluk = row_dict['taluk']
                    state_obj, created = State.objects.get_or_create(
                        unique_id=state_name.strip().lower()
                        )
                    if created:
                        state_obj.name=state_name
                        state_obj.save()
                    unique_id= "%s_%s" % (district, state_name)
                    district_obj, created = District.objects.get_or_create(
                        unique_id=unique_id.lower(),
                        state=state_obj)
                    if created:
                        district_obj.name=district
                        district_obj.save()
                    unique_id= "%s_%s_%s" % (taluk, district, state_name)
                    taluk_obj, created = Taluk.objects.get_or_create(
                        unique_id=unique_id.lower(),
                        district=district_obj,
                        state=state_obj)
                    if created:
                        taluk_obj.name=taluk
                        taluk_obj.save()
                    unique_id= "%s_%s_%s_%s" % (village_name, taluk, district, state_name)
                    village_obj, created = Village.objects.get_or_create(
                        unique_id= unique_id.lower(),
                        taluk=taluk_obj,
                        district=district_obj,
                        state=state_obj)
                    if created:
                        village_obj.name=village_name
                        village_obj.pincode = pincode
                        village_obj.save()
        except Exception as e:
            import pdb;pdb.set_trace()
            print(e)










