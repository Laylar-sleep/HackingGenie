%This code is executed to record the abnormal data by ThingSpeak React App
%after detection of high body temperature

peopleID = 1291936;
abnormalID = 1293111;
abWriteAPIKey = 'TO5BZIH4YEE75QOT';
%% Read Data %%
info = thingSpeakRead(peopleID, 'OutputFormat', 'matrix');
%% Write Data %%
thingSpeakWrite(abnormalID, info, 'WriteKey', abWriteAPIKey);