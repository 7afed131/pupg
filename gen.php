<?php
// اذا تخمط حط حقوقي @X888E - @E999G
$akil = 500; //<50 يعني كمبو 10k 500 يعني كمبو 100k 500 يعني كمبو 1مليون
for($x2=0;$x2<$akil; $x2++){
$vv = file_get_contents("https://combolist.org/generate");
$hh = explode("spellcheck=", $vv)[1];
$hh2 = explode("</textarea>", $hh)[0];
file_put_contents("combo.txt",$hh2."\n",FILE_APPEND); //@X888E 
$is  = explode("\n",file_get_contents("combo.txt"));
$iss = count($is)-1;
echo "done < $iss > BY @X888E \n";
}
// اذا تخمط حط حقوقي @X888E - @E999G