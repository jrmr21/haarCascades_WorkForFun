# haarCascades_WorkForFun
Harrcascades_workForFun


make your sample :
	opencv_createsamples -img example.jpg -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.5 -num 1900
	
make vector file :
	sudo opencv_createsamples -info info.txt -num 894 -w 40 -h 40 -vec positives.vec
	
learning :
	sudo opencv_traincascade -data out_train -vec positives.vec -bg bg.txt -numstages 10 -minHitRate 0.999 -numPos 850 -numNeg 367 -maxFalseAlarmRate 0.5 -w 40 -h 40 -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024
