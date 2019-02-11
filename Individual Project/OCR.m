clc; clear;

% Read the image
I = imread('licenseplate1.jpg');

results = ocr(I, 'TextLayout', 'Block', 'Language','licenseplate/tessdata/licenseplate.traineddata' );

recognisedText = results.Text

fid = fopen('textoutput.txt','wt');
fprintf(fid,'%f\n',recognisedText);
fclose(fid);

