from django.db import models
from django.contrib.auth.models import User
import datetime

APPLICATION_STATUSES = (
    (0, 'Start'),
    (1, 'Step 1'),
    (2, 'Complete'),
)

PAY_FREQUENCIES = (
    (1, 'Weekly'),
    (2, 'Bi-Weekly'),
    (3, '2x Month'),
    (4, 'Monthly')
)

ETHNICITIES = (
    ('Hispanic or Latino', 'Hispanic or Latino'),
    ('Not Hispanic or Latino', 'Not Hispanic or Latino'),
)

YES_NO = (
    (True, 'Yes',),
    (False, 'No',)
)


class Application(models.Model):
    applications = models.Manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=APPLICATION_STATUSES, verbose_name='Application Status',
                                 help_text='Application Status', default=0)
    last_page = models.CharField(max_length=50, verbose_name='Last Page', blank=True, null=True)
    enabled = models.BooleanField(verbose_name='Enabled', default=True)
    create_date = models.DateField(verbose_name='Create date')
    modified_date = models.DateField(verbose_name='Last modified date', blank=True, null=True)
    total_household_members = models.IntegerField(verbose_name='Total Household Members',
                                                  help_text='Total household members including children and adults',
                                                  blank=True, null=True)

    assistance_program = models.BooleanField(verbose_name='Participate in Assistance Program', choices=YES_NO,
                                             default=False)
    ssn_four_digit = models.CharField(max_length=4,
                                      verbose_name='Last 4 digits of SSN',
                                      help_text='Last four digits of the Social Security number of an '
                                                'adult household member',
                                      blank=True,
                                      null=True)
    no_ssn = models.BooleanField(verbose_name='Check if No SSN', default=False)
    case_number = models.CharField(max_length=50,
                                   verbose_name='Case Number', blank=True, null=True)

    first_name = models.CharField(max_length=25,
                                  verbose_name='First Name', blank=True, null=True)
    last_name = models.CharField(max_length=25,
                                 verbose_name='Last Name', blank=True, null=True)
    middle_name = models.CharField(max_length=25,
                                   verbose_name='Middle Name',
                                   blank=True,
                                   null=True)
    signature = models.CharField(max_length=75,
                                 verbose_name='Signature', blank=True, null=True)
    todays_date = models.DateField(verbose_name='Todays Date', blank=True, null=True)
    street_address = models.CharField(max_length=255,
                                      verbose_name='Street Address', blank=True, null=True)
    apt = models.CharField(max_length=10,
                           verbose_name='Apartment Number', blank=True, null=True)
    city = models.CharField(max_length=75,
                            verbose_name='City', blank=True, null=True)
    state = models.CharField(max_length=50,
                             verbose_name='State', blank=True, null=True)
    zip = models.CharField(max_length=10,
                           verbose_name='Zip', blank=True, null=True)
    phone = models.CharField(max_length=15,
                             verbose_name='Phone', blank=True, null=True)
    email = models.CharField(max_length=255,
                             verbose_name='Email', blank=True, null=True),
    ethnicity = models.CharField(max_length=25, choices=ETHNICITIES,
                                 verbose_name='Ethnicity', blank=True, null=True)
    is_american_indian = models.NullBooleanField(verbose_name='Is American Indian or Alaskan Native')
    is_asian = models.NullBooleanField(verbose_name='Is Asian')
    is_black = models.NullBooleanField(verbose_name='Is Black or African American')
    is_hawaiian = models.NullBooleanField(verbose_name='Is Hawaiian or Other Pacific Islander')
    is_white = models.NullBooleanField(verbose_name='Is White')
    active = models.BooleanField(verbose_name='Active', default=True)


class Child(models.Model):
    children = models.Manager()
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25,
                                  verbose_name='First Name')
    last_name = models.CharField(max_length=25,
                                 verbose_name='Last Name')
    middle_name = models.CharField(max_length=25,
                                   verbose_name='Middle Name',
                                   blank=True,
                                   null=True)
    is_student = models.BooleanField(verbose_name='Is Student')
    foster_child = models.BooleanField(verbose_name='Is Foster Child')
    hmr = models.BooleanField(verbose_name='Homeless, Migrant, Runaway')
    salary = models.IntegerField(verbose_name='Salary',
                                 help_text='Salary or Wages from a Job',
                                 blank=True,
                                 null=True)
    salary_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                           verbose_name='Frequency Of Salary',
                                           help_text='How often are earnings received',
                                           blank=True,
                                           null=True)
    ssi_disability = models.IntegerField(verbose_name='Social Security Income for Disability',
                                         help_text='Social security income for childs blindness or disability',
                                         blank=True,
                                         null=True)
    ssi_disability_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Frequency Of Social Security Income for Disability',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    ssi_parent_disability = models.IntegerField(verbose_name='Social Security Income for Parents Disability',
                                                help_text='Social security income received if parent is disabled/retired/deceased',
                                                blank=True,
                                                null=True)
    ssi_parent_disability_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                          verbose_name='Frequency Of Social Security Income for Parent Disabilty',
                                                          help_text='How often are earnings received',
                                                          blank=True,
                                                          null=True)
    spending_money_income = models.IntegerField(verbose_name='Spending Money Income',
                                                help_text='Spending money received from a person outside the household',
                                                blank=True,
                                                null=True)
    spending_money_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                          verbose_name='Frequency Of Spending Money Income',
                                                          help_text='How often are earnings received',
                                                          blank=True,
                                                          null=True)
    other_friend_income = models.IntegerField(verbose_name='Other Regular Income From Friends',
                                              blank=True,
                                              null=True)
    other_friend_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                        verbose_name='Frequency Of Other Regular Income From Friends',
                                                        help_text='How often are earnings received',
                                                        blank=True,
                                                        null=True)
    pension_income = models.IntegerField(verbose_name='Pension Income',
                                         blank=True,
                                         null=True)
    pension_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Pension Income Frequency',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    annuity_income = models.IntegerField(verbose_name='Annuity Income',
                                         blank=True,
                                         null=True)
    annuity_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Annuity Income Frequency',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    trust_income = models.IntegerField(verbose_name='Trust Income',
                                       blank=True,
                                       null=True)
    trust_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                 verbose_name='Trust Income Frequency',
                                                 help_text='How often are earnings received',
                                                 blank=True,
                                                 null=True)
    other_income = models.IntegerField(verbose_name='Other Income',
                                       help_text='Any other income',
                                       blank=True,
                                       null=True)
    other_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                 verbose_name='Other Income Frequency',
                                                 help_text='How often are earnings received',
                                                 blank=True,
                                                 null=True)


class Adult(models.Model):
    adults = models.Manager()
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25,
                                  verbose_name='First Name')
    middle_name = models.CharField(max_length=25,
                                   verbose_name='Middle Name', blank=True, null=True)
    last_name = models.CharField(max_length=25,
                                 verbose_name='Last Name')
    salary = models.IntegerField(verbose_name='Salary',
                                 help_text='Salary from a Job',
                                 blank=True,
                                 null=True)
    salary_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                           verbose_name='Frequency Of Salary',
                                           help_text='How often are earnings received',
                                           blank=True,
                                           null=True)
    wages = models.IntegerField(verbose_name='Wages',
                                help_text='Wages from a Job',
                                blank=True,
                                null=True)
    wages_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                          verbose_name='Frequency Of Wages',
                                          help_text='How often are earnings received',
                                          blank=True,
                                          null=True)
    cash_bonuses = models.IntegerField(verbose_name='Cash Bonuses',
                                       blank=True,
                                       null=True)
    cash_bonuses_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                 verbose_name='Frequency Of Cash Bonuses',
                                                 help_text='How often are earnings received',
                                                 blank=True,
                                                 null=True)
    self_employment_income = models.IntegerField(verbose_name='Self Employment Income',
                                                 help_text='Net income from self employment',
                                                 blank=True,
                                                 null=True)
    self_employment_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                           verbose_name='Frequency Of Self Employment Income',
                                                           help_text='How often are earnings received',
                                                           blank=True,
                                                           null=True)
    strike_benefits = models.IntegerField(verbose_name='Strike Benefits',
                                          blank=True,
                                          null=True)
    strike_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                    verbose_name='Frequency Of Strike Benefits',
                                                    help_text='How often are earnings received',
                                                    blank=True,
                                                    null=True)
    unemployment_insurance = models.IntegerField(verbose_name='Unemployment Insurance',
                                                 blank=True,
                                                 null=True)
    unemployment_insurance_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                           verbose_name='Frequency Of Unemployment Insurance',
                                                           help_text='How often are earnings received',
                                                           blank=True,
                                                           null=True)
    other_earned_income = models.IntegerField(verbose_name='Other Earned Income',
                                              blank=True,
                                              null=True)
    other_earned_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                        verbose_name='Frequency Of Other Earned Income',
                                                        help_text='How often are earnings received',
                                                        blank=True,
                                                        null=True)
    military_basic_pay = models.IntegerField(verbose_name='Military Basic Pay',
                                             blank=True,
                                             null=True)
    military_basic_pay_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of Military Basic Pay',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    military_bonus = models.IntegerField(verbose_name='Military Bonus',
                                         blank=True,
                                         null=True)
    military_bonus_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Frequency Of Military Bonus',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    military_allowance = models.IntegerField(verbose_name='Military Allowance',
                                             blank=True,
                                             null=True)
    military_allowance_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of Military Allowance',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    military_food = models.IntegerField(verbose_name='Military Food',
                                        blank=True,
                                        null=True)
    military_food_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                  verbose_name='Frequency Of Military Food',
                                                  help_text='How often are earnings received',
                                                  blank=True,
                                                  null=True)
    military_clothing = models.IntegerField(verbose_name='Military Clothing',
                                            blank=True,
                                            null=True)
    military_clothing_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                      verbose_name='Frequency Of Military Clothing',
                                                      help_text='How often are earnings received',
                                                      blank=True,
                                                      null=True)
    general_assistance = models.IntegerField(verbose_name='General Assistance',
                                             help_text='General assistance excluding SNAP or TANF',
                                             blank=True,
                                             null=True)
    general_assistance_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of General Assistance',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    cash_assistance = models.IntegerField(verbose_name='Cash assistance from State or local government',
                                           blank=True,
                                           null=True)
    cash_assistance_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                     verbose_name='Frequency Of Csah Assistance',
                                                     help_text='How often are earnings received',
                                                     blank=True,
                                                     null=True)
    alimony = models.IntegerField(verbose_name='Alimony Received',
                                  blank=True,
                                  null=True)
    alimony_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                            verbose_name='Frequency Of Alimony',
                                            help_text='How often are earnings received',
                                            blank=True,
                                            null=True)
    child_support = models.IntegerField(verbose_name='Child Support',
                                        blank=True,
                                        null=True)
    child_support_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                  verbose_name='Frequency Of Child Support',
                                                  help_text='How often are earnings received',
                                                  blank=True,
                                                  null=True)
    social_security_income = models.IntegerField(verbose_name='Social Security Income',
                                                 blank=True,
                                                 null=True)
    social_security_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                           verbose_name='Frequency Of Social Security Income',
                                                           help_text='How often are earnings received',
                                                           blank=True,
                                                           null=True)
    railroad_income = models.IntegerField(verbose_name='Railroad Retirement Income',
                                          blank=True,
                                          null=True)
    railroad_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                    verbose_name='Frequency Of Railroad Retirement Income',
                                                    help_text='How often are earnings received',
                                                    blank=True,
                                                    null=True)
    pension_income = models.IntegerField(verbose_name='Pension Income',
                                         blank=True,
                                         null=True)
    pension_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Frequency Of Pension Income',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    annuity_income = models.IntegerField(verbose_name='Annuity Income',
                                         blank=True,
                                         null=True)
    annuity_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Frequency Of Annuity Income',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    survivors_benefits = models.IntegerField(verbose_name='Survivor''s Benefits',
                                             blank=True,
                                             null=True)
    survivors_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                       verbose_name='Frequency Of Survivor''s Benefits',
                                                       help_text='How often are earnings received',
                                                       blank=True,
                                                       null=True)
    ssi_disability_benefits = models.IntegerField(verbose_name='Disability Benefits From Supplemental Security Income',
                                                  blank=True,
                                                  null=True)
    ssi_disability_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                            verbose_name='Frequency Of SSI Disability Benefits',
                                                            help_text='How often are earnings received',
                                                            blank=True,
                                                            null=True)
    private_disability_benefits = models.IntegerField(verbose_name='Private Disability Benefits',
                                                      blank=True,
                                                      null=True)
    private_disability_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                                verbose_name='Frequency Of Private Disability Benefits',
                                                                help_text='How often are earnings received',
                                                                blank=True,
                                                                null=True)
    black_lung_benefits = models.IntegerField(verbose_name='Black Lung Benefits',
                                              blank=True,
                                              null=True)
    black_lung_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                        verbose_name='Frequency Of Black Lung Benefits',
                                                        help_text='How often are earnings received',
                                                        blank=True,
                                                        null=True)
    workers_compensation = models.IntegerField(verbose_name='Worker''s Compensation',
                                               blank=True,
                                               null=True)
    workers_compensation_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                         verbose_name='Frequency Of Worker''s Compensation',
                                                         help_text='How often are earnings received',
                                                         blank=True,
                                                         null=True)
    veterans_benefits = models.IntegerField(verbose_name='Veteran''s Benefits',
                                            blank=True,
                                            null=True)
    veterans_benefits_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                      verbose_name='Frequency Of Veteran''s Benefits',
                                                      help_text='How often are earnings received',
                                                      blank=True,
                                                      null=True)
    other_retirement_sources = models.IntegerField(verbose_name='Other Retirement Sources',
                                                   blank=True,
                                                   null=True)
    other_retirement_sources_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                             verbose_name='Frequency Of Other Retirement Sources',
                                                             help_text='How often are earnings received',
                                                             blank=True,
                                                             null=True)
    interest_income = models.IntegerField(verbose_name='Interest Income',
                                          blank=True,
                                          null=True)
    interest_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                    verbose_name='Frequency Of Interest Income',
                                                    help_text='How often are earnings received',
                                                    blank=True,
                                                    null=True)
    investment_income = models.IntegerField(verbose_name='Investment Income',
                                          blank=True,
                                          null=True)
    investment_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                    verbose_name='Frequency Of Investment Income',
                                                    help_text='How often are earnings received',
                                                    blank=True,
                                                    null=True)
    dividends = models.IntegerField(verbose_name='Dividends',
                                    blank=True,
                                    null=True)
    dividends_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                              verbose_name='Frequency Of Dividends',
                                              help_text='How often are earnings received',
                                              blank=True,
                                              null=True)
    trust_or_estates_income = models.IntegerField(verbose_name='Trust Or Estates Income',
                                                  blank=True,
                                                  null=True)
    trust_or_estates_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                            verbose_name='Frequency Of Trust Or Estates Income',
                                                            help_text='How often are earnings received',
                                                            blank=True,
                                                            null=True)
    rental_income = models.IntegerField(verbose_name='Rental Income',
                                        blank=True,
                                        null=True)
    rental_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                  verbose_name='Frequency Of Rental Income',
                                                  help_text='How often are earnings received',
                                                  blank=True,
                                                  null=True)
    royalties_income = models.IntegerField(verbose_name='Royalties Income',
                                           blank=True,
                                           null=True)
    royalties_income_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                     verbose_name='Frequency Of Royalties Income',
                                                     help_text='How often are earnings received',
                                                     blank=True,
                                                     null=True)
    prize_winnings = models.IntegerField(verbose_name='Prize Winnings',
                                         blank=True,
                                         null=True)
    prize_winnings_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                   verbose_name='Frequency Of Prize Winnings',
                                                   help_text='How often are earnings received',
                                                   blank=True,
                                                   null=True)
    savings_withdrawn = models.IntegerField(verbose_name='Savings Withdrawn',
                                            blank=True,
                                            null=True)
    savings_withdrawn_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                                      verbose_name='Frequency Of Savings Withdrawn',
                                                      help_text='How often are earnings received',
                                                      blank=True,
                                                      null=True)
    cash_gifts = models.IntegerField(verbose_name='Cash Gifts from Friends',
                                     blank=True,
                                     null=True)
    cash_gifts_frequency = models.IntegerField(choices=PAY_FREQUENCIES,
                                               verbose_name='Frequency Of Cash Gifts',
                                               help_text='How often are earnings received',
                                               blank=True, null=True)


class EarningSource(models.Model):
    sources = models.Manager()
    name = models.CharField(max_length=50, verbose_name='Source')

    def __str__(self):
        return self.name


class EarningsPage(models.Model):
    entity = models.CharField(max_length=50,
                                choices=(('child', 'Child',), ('adult', 'Adult',)),
                                verbose_name='Entity')
    name = models.CharField(max_length=50, verbose_name='Page name')
    page_arg = models.CharField(max_length=50,
                                choices=(('child_id', 'child_id',), ('adult_id', 'adult_id',)),
                                verbose_name='Page Argument', blank=True, null=True)
    source = models.ForeignKey(EarningSource, blank=True, null=True)
    page_type = models.CharField(max_length=20,
                                 choices=(('form', 'Form',),
                                          ('confirmation', 'Confirmation',),
                                          ('summary', 'Summary',)),
                                 verbose_name='Page Type', default='form')
    value_field = models.CharField(max_length=50, verbose_name='Value Field', blank=True, null=True)
    frequency_field = models.CharField(max_length=50, verbose_name='Frequency Field', blank=True, null=True)
    display_title = models.CharField(max_length=100, verbose_name='Display Title', blank=True, null=True)
    headline = models.CharField(max_length=500, verbose_name='Page Headline', blank=True, null=True)
    help_tip = models.CharField(max_length=1000, verbose_name='Help tip', blank=True, null=True)
    template = models.CharField(max_length=500, verbose_name='Template path',
                                default='eat/user/application/child/earnings.html')
    next = models.ForeignKey('self', blank=True, null=True, related_name='next_page')
    skip_to = models.ForeignKey('self', blank=True, null=True, related_name='skip_page')

    def __str__(self):
        return '%s.%s' % (self.entity, self.name)
