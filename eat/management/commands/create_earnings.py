from django.core.management.base import BaseCommand, CommandError
from eat.models import EarningsPage
from eat import child_earnings_meta_data, adult_earnings_meta_data


class Command(BaseCommand):
    help = "Creates the earnings pages meta data table"

    def handle(self, *args, **options):

        EarningsPage.objects.all().delete()

        for k, v in child_earnings_meta_data.items():
            e = EarningsPage(entity='child',
                name=v['name'],
                page_arg='child_id',
                page_type=v['type'],
                value_field=v['value_field'] if 'value_field' in v else None,
                frequency_field=v['frequency_field'] if 'frequency_field' in v else None,
                display_title=v['title'],
                headline=v['headline'] if 'headline' in v else None,
                template=v['template']
            )
            e.save()
            self.stdout.write(self.style.SUCCESS(v['title']))

        for k, v in adult_earnings_meta_data.items():

            e = EarningsPage(entity='adult',
                name=v['name'],
                page_arg='adult_id',
                page_type='form' if 'value_field' in v else 'confirmation',
                value_field=v['value_field'] if 'value_field' in v else None,
                frequency_field=v['frequency_field'] if 'frequency_field' in v else None,
                display_title=v['title'],
                headline=v['headline'] if 'headline' in v else None,
                template=v['template']
            )
            e.save()
            self.stdout.write(self.style.SUCCESS(v['title']))