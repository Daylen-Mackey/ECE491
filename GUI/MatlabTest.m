T = readtable('Test.csv');
X = T{:,:};
csvwrite('MatlabTest.csv',X);
