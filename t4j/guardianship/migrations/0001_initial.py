# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualReport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ward_county', models.CharField(default=b'Harris', max_length=20, choices=[(b'ANDERSON', b'Anderson'), (b'ANDREWS', b'Andrews'), (b'ANGELINA', b'Angelina'), (b'ARANSAS', b'Aransas'), (b'ARCHER', b'Archer'), (b'ARMSTRONG', b'Armstrong'), (b'ATASCOSA', b'Atascosa'), (b'AUSTIN', b'Austin'), (b'BAILEY', b'Bailey'), (b'BANDERA', b'Bandera'), (b'BASTROP   ', b'Bastrop'), (b'BAYLOR', b'Baylor'), (b'BEE', b'Bee'), (b'BELL', b'Bell'), (b'BEXAR', b'Bexar'), (b'BLANCO', b'Blanco'), (b'BORDEN', b'Borden'), (b'BOSQUE', b'Bosque'), (b'BOWIE', b'Bowie'), (b'BRAZORIA', b'Brazoria'), (b'BRAZOS', b'Brazos'), (b'BREWSTER', b'Brewster'), (b'BRISCOE', b'Briscoe'), (b'BROOKS', b'Brooks'), (b'BROWN', b'Brown'), (b'BURLESON', b'Burleson'), (b'BURNET', b'Burnet'), (b'CALDWELL', b'Caldwell'), (b'CALHOUN', b'Calhoun'), (b'CALLAHAN', b'Callahan'), (b'CAMERON', b'Cameron'), (b'CAMP', b'Camp'), (b'CARSON', b'Carson'), (b'CASS', b'Cass'), (b'CASTRO', b'Castro'), (b'CHAMBERS', b'Chambers'), (b'CHEROKEE', b'Cherokee'), (b'CHILDRESS', b'Childress'), (b'CLAY', b'Clay'), (b'COCHRAN', b'Cochran'), (b'COKE', b'Coke'), (b'COLEMAN', b'Coleman'), (b'COLLIN', b'Collin'), (b'COLLINGSWORTH', b'Collingsworth'), (b'COLORADO', b'Colorado'), (b'COMAL', b'Comal'), (b'COMANCHE', b'Comanche'), (b'CONCHO', b'Concho'), (b'COOKE', b'Cooke'), (b'CORYELL', b'Coryell'), (b'COTTLE', b'Cottle'), (b'CRANE', b'Crane'), (b'CROCKETT', b'Crockett'), (b'CROSBY', b'Crosby'), (b'CULBERSON', b'Culberson'), (b'DALLAM', b'Dallam'), (b'DALLAS', b'Dallas'), (b'DAWSON', b'Dawson'), (b'DE WITT', b'De Witt'), (b'DEAF SMITH', b'Deaf Smith'), (b'DELTA', b'Delta'), (b'DENTON', b'Denton'), (b'DICKENS', b'Dickens'), (b'DIMMIT', b'Dimmit'), (b'DONLEY', b'Donley'), (b'DUVAL', b'Duval'), (b'EASTLAND', b'Eastland'), (b'ECTOR', b'Ector'), (b'EDWARDS', b'Edwards'), (b'EL PASO', b'El Paso'), (b'ELLIS', b'Ellis'), (b'ERATH', b'Erath'), (b'FALLS', b'Falls'), (b'FANNIN', b'Fannin'), (b'FAYETTE', b'Fayette'), (b'FISHER', b'Fisher'), (b'FLOYD', b'Floyd'), (b'FOARD', b'Foard'), (b'FORT BEND', b'Fort Bend'), (b'FRANKLIN', b'Franklin'), (b'FREESTONE', b'Freestone'), (b'FRIO', b'Frio'), (b'GAINES', b'Gaines'), (b'GALVESTON', b'Galveston'), (b'GARZA', b'Garza'), (b'GILLESPIE', b'Gillespie'), (b'GLASSCOCK', b'Glasscock'), (b'GOLIAD', b'Goliad'), (b'GONZALES', b'Gonzales'), (b'GRAY', b'Gray'), (b'GRAYSON', b'Grayson'), (b'GREGG', b'Gregg'), (b'GRIMES', b'Grimes'), (b'GUADALUPE', b'Guadalupe'), (b'HALE', b'Hale'), (b'HALL', b'Hall'), (b'HAMILTON', b'Hamilton'), (b'HANSFORD', b'Hansford'), (b'HARDEMAN', b'Hardeman'), (b'HARDIN', b'Hardin'), (b'HARRIS', b'Harris'), (b'HARRISON', b'Harrison'), (b'HARTLEY', b'Hartley'), (b'HASKELL', b'Haskell'), (b'HAYS', b'Hays'), (b'HEMPHILL', b'Hemphill'), (b'HENDERSON', b'Henderson'), (b'HIDALGO', b'Hidalgo'), (b'HILL', b'Hill'), (b'HOCKLEY', b'Hockley'), (b'HOOD', b'Hood'), (b'HOPKINS', b'Hopkins'), (b'HOUSTON', b'Houston'), (b'HOWARD', b'Howard'), (b'HUDSPETH', b'Hudspeth'), (b'HUNT', b'Hunt'), (b'HUTCHINSON', b'Hutchinson'), (b'IRION', b'Irion'), (b'JACK', b'Jack'), (b'JACKSON', b'Jackson'), (b'JASPER', b'Jasper'), (b'JEFF DAVIS', b'Jeff Davis'), (b'JEFFERSON', b'Jefferson'), (b'JIM HOGG', b'Jim Hogg'), (b'JIM WELLS', b'Jim Wells'), (b'JOHNSON', b'Johnson'), (b'JONES', b'Jones'), (b'KARNES', b'Karnes'), (b'KAUFMAN', b'Kaufman'), (b'KENDALL', b'Kendall'), (b'KENEDY', b'Kenedy'), (b'KENT', b'Kent'), (b'KERR   ', b'Kerr   '), (b'KIMBLE', b'Kimble'), (b'KING', b'King'), (b'KINNEY', b'Kinney'), (b'KLEBERG', b'Kleberg'), (b'KNOX', b'Knox'), (b'LA SALLE', b'La Salle'), (b'LAMAR', b'Lamar'), (b'LAMB', b'Lamb'), (b'LAMPASAS', b'Lampasas'), (b'LAVACA', b'Lavaca'), (b'LEE', b'Lee'), (b'LEON', b'Leon'), (b'LIBERTY', b'Liberty'), (b'LIMESTONE', b'Limestone'), (b'LIPSCOMB', b'Lipscomb'), (b'LIVE OAK', b'Live Oak'), (b'LLANO', b'Llano'), (b'LOVING', b'Loving'), (b'LUBBOCK', b'Lubbock'), (b'LYNN', b'Lynn'), (b'MADISON', b'Madison'), (b'MARION', b'Marion'), (b'MARTIN', b'Martin'), (b'MASON', b'Mason'), (b'MATAGORDA', b'Matagorda'), (b'MAVERICK', b'Maverick'), (b'MCCULLOCH', b'McCulloch'), (b'MCLENNAN', b'McLennan'), (b'MCMULLEN', b'McMullen'), (b'MEDINA', b'Medina'), (b'MENARD', b'Menard'), (b'MIDLAND', b'Midland'), (b'MILAM', b'Milam'), (b'MILLS', b'Mills'), (b'MITCHELL', b'Mitchell'), (b'MONTAGUE', b'Montague'), (b'MONTGOMERY', b'Montgomery'), (b'MOORE', b'Moore'), (b'MORRIS', b'Morris'), (b'MOTLEY', b'Motley'), (b'NACOGDOCHES', b'Nacogdoches'), (b'NAVARRO', b'Navarro'), (b'NEWTON', b'Newton'), (b'NOLAN', b'Nolan'), (b'NUECES', b'Nueces'), (b'OCHILTREE', b'Ochiltree'), (b'OLDHAM', b'Oldham'), (b'ORANGE', b'Orange'), (b'PALO PINTO', b'Palo Pinto'), (b'PANOLA', b'Panola'), (b'PARKER ', b'Parker '), (b'PARMER', b'Parmer'), (b'PECOS', b'Pecos'), (b'POLK', b'Polk'), (b'POTTER', b'Potter'), (b'PRESIDIO', b'Presidio'), (b'RAINS', b'Rains'), (b'RANDALL', b'Randall'), (b'REAGAN', b'Reagan'), (b'REAL', b'Real'), (b'RED RIVER', b'Red River'), (b'REEVES', b'Reeves'), (b'REFUGIO', b'Refugio'), (b'ROBERTS', b'Roberts'), (b'ROBERTSON', b'Robertson'), (b'ROCKWALL', b'Rockwall'), (b'RUNNELS', b'Runnels'), (b'RUSK', b'Rusk'), (b'SABINE', b'Sabine'), (b'SAN AUGUSTINE', b'San Augustine'), (b'SAN JACINTO', b'San Jacinto'), (b'SAN PATRICIO', b'San Patricio'), (b'SAN SABA', b'San Saba'), (b'SCHLEICHER', b'Schleicher'), (b'SCURRY', b'Scurry'), (b'SHACKELFORD', b'Shackelford'), (b'SHELBY', b'Shelby'), (b'SHERMAN', b'Sherman'), (b'SMITH', b'Smith'), (b'SOMERVELL', b'Somervell'), (b'STARR', b'Starr'), (b'STEPHENS', b'Stephens'), (b'STERLING', b'Sterling'), (b'STONEWALL', b'Stonewall'), (b'SUTTON', b'Sutton'), (b'SWISHER', b'Swisher'), (b'TARRANT', b'Tarrant'), (b'TAYLOR', b'Taylor'), (b'TERRELL', b'Terrell'), (b'TERRY', b'Terry'), (b'THROCKMORTON', b'Throckmorton'), (b'TITUS', b'Titus'), (b'TOM GREEN', b'Tom Green'), (b'TRAVIS', b'Travis'), (b'TRINITY', b'Trinity'), (b'TYLER', b'Tyler'), (b'UPSHUR', b'Upshur'), (b'UPTON', b'Upton'), (b'UVALDE', b'Uvalde'), (b'VAL VERDE', b'Val Verde'), (b'VAN ZANDT', b'Van Zandt'), (b'VICTORIA', b'Victoria'), (b'WALKER', b'Walker'), (b'WALLER', b'Waller'), (b'WARD', b'Ward'), (b'WASHINGTON', b'Washington'), (b'WEBB', b'Webb'), (b'WHARTON ', b'Wharton '), (b'WHEELER', b'Wheeler'), (b'WICHITA', b'Wichita'), (b'WILBARGER', b'Wilbarger'), (b'WILLACY', b'Willacy'), (b'WILLIAMSON', b'Williamson'), (b'WILSON', b'Wilson'), (b'WINKLER', b'Winkler'), (b'WISE', b'Wise'), (b'WOOD', b'Wood'), (b'YOAKUM', b'Yoakum'), (b'YOUNG', b'Young'), (b'ZAPATA', b'Zapata'), (b'ZAVAL', b'Zaval')])),
                ('docket_number', models.CharField(help_text=b'This is the case number that the court uses to identify the case.', max_length=30)),
                ('ward_name', models.CharField(help_text=b'The full name (including middle name) of the person under guardianship.', max_length=50)),
                ('ward_dob', models.DateField(help_text=b'Please use the following format: <em>YYYY-MM-DD</em>.')),
                ('ward_current_age', models.IntegerField(help_text=b'The current age (in years) of the person under guardianship.')),
                ('wards_residence', models.CharField(default=b"Guardian's home", max_length=20, choices=[(b"Guardian's home", b"Guardian's home"), (b'Foster or boarding home', b'Foster or boarding home'), (b'Hospital or medical facility', b'Hospital or medical facility'), (b'Nursing home', b'Nursing home '), (b"Relative's home", b"Relative's home"), (b'Other', b'Other')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
