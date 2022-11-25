create table ho_simpleTable(
	st_name varchar2(10 char) primary key, 
	st_price number(5) not null
);

select * from HO_SIMPLETABLE;

select * from HO_SIMPLETABLE where st_price = (select min(st_price) from HO_SIMPLETABLE);

create table ho_kmaData(
	hk_time number(2) not null,
	hk_temp number(3, 1) not null,
	hk_weather varchar2(6 char) not null,
	hk_date date not null
);

select * from ho_kmaData;
delete ho_kmaData;

select avg(hk_temp) from ho_kmaData group by hk_hour order by hk_hour

create table ho_subwayData(
	hs_line varchar2(10 char) not null,
	hs_station varchar2(10 char) not null,
	hs_ride_PASGR number(6) not null,
	hs_ALIGHT_PASGR number(6) not null
);

drop table ho_simpleTable cascade constraint purge;
select * from ho_subwayData

create table ho_openWeatherData(
	ho_weather varchar2(5 char) not null,
	ho_temp number(4, 2) not null,
	ho_humidity number(2) not null,
	ho_date date not null
);
"KW_WFKOR"
select * from ho_openWeatherData
select * from kma_weather_kwon
select * from owm_weather_kwon


create table haheeho_contentTable(
	hct_url varchar2(100 char) primary key,
	hct_no number(5) not null,
	hct_like number(4) not null,
	
);