Title: Lista de hashes MD5 y SHA256 de ejecutables PSTools
Date: 2020-05-13 11:35
Category: Security
Tags: PSTools, Integrity
Slug: md5-y-sha256-hash-pstools
Authors: J.R. Lambea
Summary: Puede darse el caso que una aplicación teóricamente lícita sea detectado por un antivirus como ransomware (p.e. `psexec.exe`). En este artículo se presenta una lista de referencia con hashes para todos los binarios de la suite PSTools para poder comparar y poder descartar falsos positivos.

<!-- Modified: 2010-12-05 19:30 -->

Este post surge por la problemática de tener que validar si un binario corresponde a la herramienta de PSTools original, la dificultad de encontrar un sitio fiable en la que aparezca una lista de hashes de forma que pueda saber si un fichero copiado en un servidor (por ejemplo `psexec.exe`) corresponde a una versión original e inalterada o bien a un binario que deberíamos descartar.

El listado corresponde a la última versión a dia de la escritura de este post, la 2.45:

|Binary|md5|sha256|
|---|---|---|
|PsExec.exe       |27304B246C7D5B4E149124D5F93C5B01| 3337E3875B05E0BFBA69AB926532E3F179E8CFBF162EBB60CE58A0281437A7EF|
|PsExec64.exe     |9321C107D1F7E336CDA550A2BF049108| AD6B98C01EE849874E4B4502C3D7853196F6044240D3271E4AB3FC6E3C08E9A4|
|psfile.exe       |201058594991D79D5D8891DBBEEEE3C6| 9D45453285FF3B4A41056317C96866D06481751307D703E3355B18D5EEB092AD|
|psfile64.exe     |E52AC781C403DABE22DFA16AEF8491BE| 033B81744E0BD4219A4D698894B8403BB67B525C96049CBFEF34677D4D6FC85C|
|PsGetsid.exe     |2AAF17D3C8F58DD11965ED235D7F310D| A9E3A0D0C90D440F5A7DA6DCE021C554822416C513E383409E80387E1556A760|
|PsGetsid64.exe   |7C3587312771E796BE2E65E8467FD68A| 952662A81384423ABF2E9D78DAD7CF8EC77D9B6C93D122B272211B3E6C7F8E49|
|PsInfo.exe       |624ADB0F45CBB9CADAD83C264DF98891| 8F401DC021E20FF3ABC64A2D346EF6A792A5643CA04FFD1F297E417532ACAA06|
|PsInfo64.exe     |EFA2F8F73B3559711149DFDEB8BC288E| EF5CF80C8448BF0907C634A3251CC348B1D36BB5AD8F31F23B11D12AA7F63BCB|
|pskill.exe       |8C1772C2D124E80526642BE3FBD2E8F3| 546EC58D0134EA64611E12D7E3A867793E8CB6145AC18745349408A60FC2FABE|
|pskill64.exe     |26EA3E520CB396587D32A7A01AA564BD| 75899C5ACE600406503A937EF550AB0BBD0F6E0188B9E93E206BEB1DFC79BB81|
|pslist.exe       |2C23D6223D4AFF81AC137B6989BCE05C| 9927831E111AC61FD7645BF7EFA1787DB1A3E85B6F64A274CA04B213DC27FD08|
|pslist64.exe     |A285919B3737ED691E1D029E36213050| E6901E8423DA3E54BAB25F7C90F60D3979BFA5BB61BCC46059662736253B8C72|
|PsLoggedon.exe   |E3EA271E748CCDAD6A6D3E692D6F337E| D689CB1DBD2E4C06CD15E51A6871C406C595790DDCDCD7DC8D0401C7183720EF|
|PsLoggedon64.exe |07ED30D2343BF8914DAAED872B681118| FDADB6E15C52C41A31E3C22659DD490D5B616E017D1B1AA6070008CE09ED27EA|
|psloglist.exe    |BD35132C7A1E78364F4B908EBAF8CB5D| 57DC27269669402152518DC7683E0A9CC372A3C3125EFE1C7ECD8E8516F556F3|
|psloglist64.exe  |E25ADD3F10FDC894E4C1F889350DC290| E2587DD0AA50D75B545E2100FB2BAB0B0607FF7E87B264339C7FB695B8572342|
|pspasswd.exe     |2AF538872742F9D578E5DD54D4440BA5| B2F17AB6396A5E5CD5BE12F658C22CDFA2071D377CB8BD0EE76ABBF82A9240A7|
|pspasswd64.exe   |BFEC8D28B818071DD898C1E18A98A242| B5A01628E544929E2DFF9F7041359D80F037E1E6DA8AFB97ABD6B2B2F67960C4|
|psping.exe       |829BF469365FE504C673D8B7BE7D3436| C8453110682D999223A84146462B0B4FC6979F40A01B60A7B925783B71B2D6FF|
|psping64.exe     |508657CC1D8EC7FB2155085A5691F301| 6330FD6B82B3A1C91D2396C1AC096CD2E3775CA50BAF8D223FA25A0258361126|
|PsService.exe    |02FE68328F96FEE688DA5885EB4C3CF0| 9454BA56BCB470D330559573AFBC10F6989BA46F3E656C20979DE6F92E051752|
|PsService64.exe  |029D745D114C0A69CF0CB12450CB7B74| 6DE3137B3088B2C2C311A540F9AAEB57E9FD38259CB18875F2380EE74EC1C7AF|
|psshutdown.exe   |6AA0305AF2C055AC6C94B5D24F6CEC35| 66885C2B1773A6D02C3937E67B94B786FC64AF17A7E8BAD050BE5149092A0117|
|pssuspend.exe    |DF3D77D41EF28027B3069D39F9EE9C79| 02EC8C37DD946A2CD74673993C2108F12FFF3E82019A1590231C4205CCB2F0D4|
|pssuspend64.exe  |FBE9E863C6E46F75BFABA674E3BA0CDA| E93DDD9ED564B7F6532CD5B94CDCE73067D8EBAD8A5CE9373A6F839C7050780F|
|Pstools.chm      |009AC2BE60F92DC2C41B094CE2D3857C| 2813B6C07D17D25670163E0F66453B42D2F157BF2E42007806EBC6BB9D114ACC|