%Dynamic Values
:- dynamic underlying_condition/1.
:- dynamic ethnicity/1.
:- dynamic patientn/9.
:- dynamic patientw/11.
:- dynamic punderlying/2.

%Rules
get_patientn(A,B,C,D,E,F,G,H,I):- patientn(A,B,C,D,E,F,G,H,I).
get_patientw(A,B,C,D,E,F,G,H,I,J,K):- patientw(A,B,C,D,E,F,G,H,I,J,K).
get_punderlying(A,B):- punderlying(A,B).

underlying_condition((empty)).
ethnicity((empty)).
%ethnicity('American').



