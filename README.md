# CACHEPRIMER
This utility will check if the server is up and responding with a code lower than 400 and then use Selenium to hit each page.

This approach can also be used as a baseline for Selenium based testing.

## Usage: 
Configure using environment variables to support easier docker deployments. Create or set the following environment variables:
Structure:
```
RETRIES=5               <--- How often to try. Set to 0 to go forever
WAIT=2                  <--- in seconds
PROTOCOL="http"         <--- Protocol
URL="localhost:10039"   <--- URL, including port if needed
PREFIX="/wps/portal"    <--- Path to portal
PAGES='"/woodburnstudio/home","/woodburnstudio/our-exhibitions","/woodburnstudio/our-products", ...
 ```

## Installation/Run:
This tool uses two containers, a custom build container that runs the python script to hit each page and a selenium/standalone-chrome container that is used to execute to hit each page.

Install using `docker-compose up`

To see the output use `docker-compose logs`. You should see the chrome container start, followed by the Cache Primer executing.

```
hcl-dx-cacheprimer  | *************** Cache Primer ***************
hcl-dx-cacheprimer  |  Target Server: http://localhost:10039/wps/portal
hcl-dx-cacheprimer  |  Retries: 5 Every: 2.0s
hcl-dx-cacheprimer  | --------------------------------------------
hcl-dx-cacheprimer  | Page: ,http://localhost:10039/wps/portal/woodburnstudio/home
hcl-dx-cacheprimer  | ,http://localhost:10039/wps/portal/woodburnstudio/home/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zizT1c3N0NDQwD_N3cLQwCzVy9vf2NAg1Mgo31wwkpiAJKG-AAjgZA_VFgJaaBlu4eRiZG_u5mji5AE9w9LB0NAgwMLAygCvCYUZAbYZDpqKgIALEKk_E!/dz/d5/L2dBISEvZ0FBIS9nQSEh/
hcl-dx-cacheprimer  | Page: ,http://localhost:10039/wps/portal/woodburnstudio/our-exhibitions
hcl-dx-cacheprimer  | ,http://localhost:10039/wps/portal/woodburnstudio/our-exhibitions/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zizT1c3N0NDQwD_N3cLQwCzVy9vf2NAg1MHA31w8EKTAMt3T2MTIz83c0cXYAK3D0sHQ0CDAwsDPSjiNFvgAM4Eqkfj4Io_MaH60eBleDzASEzCnJDQyMMMh0BL6GB_g!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/
...
hcl-dx-cacheprimer  | Page: ,http://localhost:10039/wps/portal/woodburnstudio/about-us
hcl-dx-cacheprimer  | ,http://localhost:10039/wps/portal/woodburnstudio/about-us/!ut/p/z1/04_Sj9CPykssy0xPLMnMz0vMAfIjo8zizT1c3N0NDQwD_N3cLQwCzVy9vf2NAg1MXAz0w8EKTAMt3T2MTIz83c0cXYAK3D0sHQ0CDAwsDPSjiNFvgAM4Eqkfj4Io_MaH60eBleDzASEzCnJDQyMMMh0BEtV0xw!!/dz/d5/L2dBISEvZ0FBIS9nQSEh/
hcl-dx-cacheprimer  | Finished
```
