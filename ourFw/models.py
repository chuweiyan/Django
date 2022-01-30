import datetime

from django.db import models
from django.utils import timezone


class CWxSandtableWeiwanggeBusiness(models.Model):
    month_id = models.TextField(blank=True, null=True)
    first_label = models.TextField(blank=True, null=True)
    second_label = models.TextField(blank=True, null=True)
    province_name = models.TextField(blank=True, null=True)
    province_code = models.TextField(blank=True, null=True)
    city_name = models.TextField(blank=True, null=True)
    city_code = models.TextField(blank=True, null=True)
    region_type = models.TextField(blank=True, null=True)
    weiwangge_name = models.TextField(blank=True, null=True)
    weiwangge_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_call_duration_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_data_all_mb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_data_frequency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_call_frequency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    province_name_bak = models.TextField(blank=True, null=True)
    city_name_bak = models.TextField(blank=True, null=True)
    user_all_call_duration_m_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                           null=True)
    user_all_data_all_mb_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_data_frequency_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_call_frequency_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_wx_sandtable_weiwangge_business'


class CWxSandtableWeiwanggeTerminal(models.Model):
    month_id = models.TextField(blank=True, null=True)
    first_label = models.TextField(blank=True, null=True)
    second_label = models.TextField(blank=True, null=True)
    province_name = models.TextField(blank=True, null=True)
    province_code = models.TextField(blank=True, null=True)
    city_name = models.TextField(blank=True, null=True)
    city_code = models.TextField(blank=True, null=True)
    region_type = models.TextField(blank=True, null=True)
    weiwangge_name = models.TextField(blank=True, null=True)
    weiwangge_area = models.FloatField(blank=True, null=True)
    user_g4_terminal_residentlocation = models.FloatField(blank=True, null=True)
    user_g5_terminal_residentlocation = models.FloatField(blank=True, null=True)
    province_name_bak = models.TextField(blank=True, null=True)
    city_name_bak = models.TextField(blank=True, null=True)
    user_g4_terminal_residentlocation_density = models.FloatField(blank=True, null=True)
    user_g5_terminal_residentlocation_density = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_wx_sandtable_weiwangge_terminal'


class CWxSandtableWeiwanggeUser(models.Model):
    month_id = models.TextField(blank=True, null=True)
    first_label = models.TextField(blank=True, null=True)
    second_label = models.TextField(blank=True, null=True)
    province_name = models.TextField(blank=True, null=True)
    province_code = models.TextField(blank=True, null=True)
    city_name = models.TextField(blank=True, null=True)
    city_code = models.TextField(blank=True, null=True)
    weiwangge_name = models.TextField(blank=True, null=True)
    weiwangge_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    region_type = models.TextField(blank=True, null=True)
    user_all_residentlocation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_g4_residentlocation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_g5_residentlocation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_g5_potential_residentlocation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                             null=True)
    user_arpuhigh_residentlocation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_terminal_price_high_residentlocation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                                    null=True)
    user_douhigh_residentlocation = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    province_name_bak = models.TextField(blank=True, null=True)
    city_name_bak = models.TextField(blank=True, null=True)
    user_all_residentlocation_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                            null=True)
    user_g4_residentlocation_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                           null=True)
    user_g5_residentlocation_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                           null=True)
    user_g5_potential_residentlocation_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                                     null=True)
    user_arpuhigh_residentlocation_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                                 null=True)
    user_terminal_price_high_residentlocation_density = models.DecimalField(max_digits=65535, decimal_places=65535,
                                                                            blank=True, null=True)
    user_douhigh_residentlocation_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                                null=True)

    class Meta:
        managed = False
        db_table = 'c_wx_sandtable_weiwangge_user'


class CWxSandtableWeiwanggeBusiness(models.Model):
    month_id = models.TextField(blank=True, null=True)
    first_label = models.TextField(blank=True, null=True)
    second_label = models.TextField(blank=True, null=True)
    province_name = models.TextField(blank=True, null=True)
    province_code = models.TextField(blank=True, null=True)
    city_name = models.TextField(blank=True, null=True)
    city_code = models.TextField(blank=True, null=True)
    region_type = models.TextField(blank=True, null=True)
    weiwangge_name = models.TextField(blank=True, null=True)
    weiwangge_area = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_call_duration_m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_data_all_mb = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_data_frequency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_call_frequency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    province_name_bak = models.TextField(blank=True, null=True)
    city_name_bak = models.TextField(blank=True, null=True)
    user_all_call_duration_m_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True,
                                                           null=True)
    user_all_data_all_mb_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_data_frequency_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    user_all_call_frequency_density = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'c_wx_sandtable_weiwangge_business'
