from tkinter import *
import tkinter as tk
#import pygame
#import wave
#pygame.init()
#deathsound = pygame.mixer.Sound("trumpet1.wav")
#levelsound = pygame.mixer.Sound("triumph.wav")
#bonussound = pygame.mixer.Sound("point.wav")
#mysterysound = pygame.mixer.Sound("pop.wav")
#killsound = pygame.mixer.Sound("snap.wav")
#pygame.mixer.music.load("eggs.mp3")
#pygame.mixer.music.play(-1)
from random import randint
from time import sleep
from math import sqrt
global play
play = True
while play == True:
    global bewegung
    global height #zeigt an, ob Mario sich im Sprung befindet
    global rundenzahl
    global sprungerlaubnis
    global bewegungserlaubnis
    global points
    global links2
    global rechts2
    global badcounter
    global badrichtung
    global leben
    global underground
    global undergroundlevel
    global lastposition
    global underposition
    global feuer
    global speed
    global feuerschonzeit
    global badfeuerschonzeit
    global badspeed
    global move
    global blocksmovecounter
    global feuerrichtungnormal
    feuerrichtungnormal = True
    blocksmovecounter = 0
    badfeuerschonzeit = 0
    todcounter = 0
    move = True
    badspeed = 3
    feuerschonzeit = 0
    speed = 12
    feuer = False
    underposition = 0
    lastposition = 0
    undergroundlevel = 1
    underground = False
    leben = 1
    badrichtung = 1
    badcounter = 0
    links2 = 0
    rechts2 = 0
    colors = list()
    points = 0
    höhe = 0
    bewegung = 0
    height = 0
    rundenzahl = 0
    sprungerlaubnis = 0
    bewegungserlaubnis = True
    mario = list()
    blocks = list()
    flag = list()
    kollisionslist = list()
    falllist = list()
    boni = list()
    boni2 = list()
    boni3 = list()
    sprunglist = list()
    bonuslist =list()
    goldlist = list()
    goldlist2 = list()
    silberlist = list()
    silberlist2 = list()
    rechts = list()
    links = list()
    badlist = list()
    badlistlinks = list()
    badlistrechts = list()
    badlistoben = list()
    baddesign = list()
    zwischendesign = list()
    switch = list()
    feuerlist = list()
    balls = list()
    balls2 = list()
    badballs = list()
    bowsercolors = list()
    bowser = list()
    bowserfeuer = list()
    zwischenbowserfeuer = list()
    bowserkill = list()
    bowserfeuercolor = list()
    buylist = list()
    hearts = list()
    blocksmove = list()
    luigi = list()
    plattform = list()
    global goodflag
    lists = (balls2, buylist, bowserfeuer,balls, bowsercolors, bowser,kollisionslist, feuerlist, falllist, boni, boni2, boni3, sprunglist, bonuslist, goldlist, goldlist2, silberlist, silberlist2, rechts, links, badlist, badlistlinks, badlistrechts, badlistoben, baddesign, zwischendesign, colors, flag, switch)
    blau1 = (213, 214, 215, 218, 219, 220, 197, 198, 199, 202, 203, 204, 182, 183, 184, 185, 186, 187, 166, 168, 169, 171, 151, 152, 153, 154, 135, 138, 119)
    braun1 = (243, 244, 245, 251, 252, 253, 254, 227, 228, 229, 235, 237, 236, 84, 85, 90, 91, 92, 93, 68, 70, 71, 75, 52, 54, 37, 38, 39)
    haut1 = (205, 206, 188, 189, 190, 163, 164, 167, 170, 173, 174, 102, 103, 104, 105, 106, 107, 108, 86, 87, 88, 89, 69, 72, 73, 74, 76, 77, 78, 53, 55, 56, 57, 59, 60, 61, 40, 41, 43)
    rot1 = (165, 172, 147, 148, 149, 150, 155, 156, 157, 158, 132, 133, 134, 136, 137, 139, 140, 141, 118, 117, 120, 121, 122, 21, 22, 23, 24, 25, 26, 27, 28, 29, 6, 7, 8, 9, 10)
    schwarz1 = (42, 58)

    rot2 = (7,8,9,10,11,22,23,24,25,26,27,28,29,30,46,47,48,62,63,64,80,95,110,111,116,117,118,119,121,122,123,125,126,132,133,134,135,136,138,139,140,150,151,152)
    haut2 = (41,42,44,54,56,57,58,60,61,62,14,15,16,31,32,70,73,74,75,77,78,79,87,88,89,90,103,104,105,106,107,108,109,170,157,113,114,115,129,130,131)
    braun2 = (38,39,40,53,55,69,71,72,76,85,86,91,92,93,94,144,160,176,181,182,192,196,197,198,212,213)
    blau2 = (120,124,137,141,153,154,155,156,158,159,167,168,169,171,172,173,174,175,183,184,185,186,187,188,189,190,191,199,200,201,202,203,204)
    schwarz2 = (43, 59)

    #weissfeuer = (213, 214, 215, 218, 219, 220, 197, 198, 199, 202, 203, 204, 182, 183, 184, 185, 186, 187, 166, 168, 169, 171, 151, 152, 153, 154, 135, 138, 119)
    rotfeuer = (168, 170)

    #weissfeuer2 = (120,124,137,141,153,154,155,156,158,159,167,168,169,171,172,173,174,175,183,184,185,186,187,188,189,190,191,199,200,201,202,203,204)
    rotfeuer2 = (170,172)

    blau3 = [220, 219, 218, 215, 214, 213, 204, 203, 202, 199, 198, 197, 187, 186, 185, 184, 183, 182, 171, 169, 168, 166, 154, 153, 152, 151, 138, 135, 122]#(118,121,134,137,150,151,152,153,154,165,167,168,170,181,182,183,184,185,186,196,197,198,199,200,201,202,203,212,213,214,217,218,219)
    braun3 = [254, 253, 252, 246, 245, 244, 243, 238, 237, 236, 230, 228, 229, 93, 92, 87, 86, 85, 84, 77, 75, 74, 70, 61, 59, 44, 43, 42]#(42,43,44,59,61,70,74,75,77,84,85,86,87,92,93,227,228,229,234,235,236,242,243,244,245,250,251,252)
    haut3 = [196, 195, 181, 180, 179, 174, 173, 170, 167, 164, 163, 107, 106, 105, 104, 103, 102, 101, 91, 90, 89, 88, 76, 73, 72, 71, 69, 68, 67, 60, 58, 57, 56, 54, 53, 52, 41, 40, 38]#(38,40,41,52,53,54,56,57,58,60,67,68,69,71,72,73,76,88,89,90,91,101,102,103,104,105,106,107,157,162,163,164,171,172,173,178,179,180,187,188, 156)
    schwarz3 = (39,55)
    rot3 = [172, 165, 158, 157, 156, 155, 150, 149, 148, 147, 141, 140, 139, 137, 136, 134, 133, 132, 123, 124, 121, 120, 119, 28, 27, 26, 25, 24, 23, 22, 21, 20, 11, 10, 9, 8, 7]#(7,8,9,10,11,20,21,22,23,24,25,26,27,28,116,117,119,120,122,123,131,132,133,135,136,138,139,140,146,147,148,149,154,155,156,157)
    weiss3 =(166,169)

    #weissfeuer3 = (118,121,134,137,150,151,152,153,154,165,167,168,170,181,182,183,184,185,186,196,197,198,199,200,201,202,203,212,213,214,217,218,219)
    rotfeuer3 = [169, 167]

    blau4 = [121, 117, 136, 132, 152, 151, 150, 149, 147, 146, 170, 169, 168, 166, 165, 164, 163, 162, 186, 185, 184, 183, 182, 181, 180, 179, 178, 202, 201, 200, 199, 198, 197]
    rot4 = [10, 9, 8, 7, 6, 27, 26, 25, 24, 23, 22, 21, 20, 19, 35, 34, 34, 51, 50, 50, 50, 82, 99, 98, 125, 124, 123, 122, 120, 119, 118, 116, 115, 141, 140, 139, 138, 137, 135, 134, 133, 155, 154, 153]
    haut4 = [40, 39, 37, 59, 57, 56, 55, 53, 52, 51, 3, 2, 2, 18, 18, 75, 72, 71, 70, 68, 67, 66, 90, 89, 88, 87, 106, 105, 104, 103, 102, 101, 100, 167, 148, 128, 127, 126, 144, 143, 142]
    schwarz4 = [38, 54]
    braun4 = [43, 42, 41, 60, 58, 76, 74, 73, 69, 92, 91, 86, 85, 84, 83, 129, 145, 161, 188, 187, 177, 205, 204, 203, 221, 220]
    rotfeuer4 = [167, 165]

    badbraun = (2, 3, 7, 8, 9, 10, 14, 15, 18, 20, 21, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35)
    badschwarz = (13, 16, 19, 22, 36, 37, 40, 41)
    badblau = (0, 1, 4, 5, 6, 11, 12, 17, 38, 39)


    bowserWeiss = (13,14,15,43,44,45,75,76,102,103,134,135,166,167,196,197,198,229,257,265,240,241,272,273,277,290,304,305,308,309,322,324,325,327,330,336,337,339,340,341,345,346,347,357,367,368,369,372)
    bowserWeiss2 = (377,378,393,398,399,400,413,429,430,431,445,455,461,462,463,470,471,472,494,495,496,497,498,499,502,503,508,509,510,531,532,540,541,559,564,565,587,593,597,607,629,633,634,635,639,650,658,661)
    bowserWeiss3 = (662,665,666,693,694,702,703,714,715,716,725,726,734,735,736,748,758,763,764,790,791,823,824,825,856,857,858,859,890,891,892,893,894,895,896,914,915,924,925,926,927,928,945,946,947,958,959,981,982,985)
    bowserWeiss4 = (986,987,1012,1013,1014,1016,1017,1018)
    bowserSchwarz = (133,162,164,165)
    bowserOrange = (46,77,78,108,109,130,161,163,193,194,195,202,225,226,227,228,233,234,235,258,259,260,263,264,266,267,292,293,294,295,299,310,331,342,343,362,363,373,374,379,394,395,410,411,425,426,456,457)
    bowserOrange2 = (488,489,504,528,529,530,535,536,542,554,555,556,561,562,563,573,574,585,586,589,590,591,594,595,617,618,621,622,623,624,639,649,652,653,654,655,656,657,667,681,684,685,686,687,688,698,699,716)
    bowserOrange3 = (458,717,718,719,720,749,750,751,766,767,795,798,883,916,917,920,921,922,923,948,949,950,951,952,953,954,955,956,957,983,984,987,988,989,990,1015,1019,1020,1021,1022,1023)

    bowserGruen = (41,42,72,73,74,104,105,106,107,110,136,137,138,139,140,141,142,168,169,170,171,172,173,174,175,199,200,201,203,204,205,206,207,230,231,232,236,237,238,239,260,261,262,265,267,268,269,270)
    bowserGruen2 = (274,275,296,297,298,300,301,302,303,306,307,311,328,329,332,333,334,335,338,344,361,364,365,366,370,371,375,376,396,397,401,402,403,404,405,406,407,408,409,412,427,428,432,433,434,435,436,437)
    bowserGruen3 = (438,439,440,441,442,443,444,459,460,464,465,466,467,468,469,473,474,475,476,477,492,493,500,501,505,506,507,526,527,533,534,537,538,539,566,567,568,569,570,571,572,596,598,599,600,601,602,603)
    bowserGruen4 = (604,605,606,627,628,630,631,632,636,637,638,659,660,663,664,668,669,670,689,690,691,692,695,696,697,700,701,721,722,723,724,727,728,729,730,731,732,733,753,754,755,756,757,759,760,761,762,765)
    bowserGruen5 = (271,785,786,787,788,789,792,793,794,796,797,799,818,819,820,821,822,826,827,828,829,830,831,851,852,853,854,855,860,861,862,863,884,885,886,887,888,889,918,919)

    ##############################Feuerbaelle############################
    bowserFeuerRot = (13,25,40,44,46,71-16,72-16,75-16,76-16,86-16,87-16,90-16,91-16,94-16,102-16,103-16,105-16,106-16,107-16,109-16,117-16,119-16,120-16,123-16,124-16,125-16)
    bowserFeuerRot2 = (185,189,190,194,195,205,206,211,212,220,221,228,229,230,235,236,246,247,248,249,250,251)
    bowserFeuerRot3 = (132-16,133-16,134-16,140-16,141-16,147-16,148-16,156-16,157-16,159-16,163-16,173-16,174-16,178-16,179-16,182-16,185-16,189-16,190-16,194-16,195-16,198-16)
    bowserOrangeFeuer = (42,52,80,88,99,102,105,106,119,120,121,122,123,133,134,135,138,139,148,149,155,156,164,171,172,180,187,188,196,197,202,203,204,213,214,215,216,217,218,219,231,232,233,234)

    bowserFeuerWeiss = (152-16,153-16,166-16,167-16,168-16,169-16,170-16,181-16,183-16,184-16,186-16,197-16,199-16,200-16,202-16,214-16,215-16,216-16,217-16)

    ebene11 = [1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ebene12 = [0,0,0,0,3,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,5,0,5,0,0,0,0,0,0,0,3,0,0,0,4]
    ebene13 = [1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,1,0,1,0,0,0,1,0,0,0,1]
    ebene14 = [0,1,0,0,0,0,1,0,0,0,3,0,0,0,0,1,1,0,0,0,0,1,0,0,0,0,1]
    ebene15 = [0,0,0,2,2,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,2,1,2]
    ebene16 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,3]
    ebene17 = [0,0,0,0,0,0,0,0,1,1,2,0,1,1]
    eben1norm = [ebene11, ebene12, ebene13, ebene14, ebene15, ebene16, ebene17]

    ebene111 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ebene112 = [0,0,0,0,3,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,5]
    ebene113 = [1]
    ebene114 = [0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    ebene1under = [ebene111, ebene112, ebene113, ebene114]

    ebene21 = [1,1,1,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ebene22 = [0,3,0,1,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    ebene23 = [0,0,0,0,3,0,1,1,1,0,0,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,1]
    ebene24 = [0,0,0,0,0,0,0,3,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1]
    ebene25 = [1,1,2,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,2,2,2,2,2,2,1]
    ebene26 = [4,0,0,1,2,0,0,0,0,0,1,1,0,0,2,2,2,0,0,1,0,3]
    ebene27 = [0,0,0,0,0,1,1,7,2,1,0,0,0,2,0,3,0,2]
    eben2norm = [ebene21, ebene22, ebene23, ebene24, ebene25, ebene26, ebene27]



    ebene31 = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ebene32 = [0,3,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,5,0,5,0,0,0,0,0,4]
    ebene33 = [0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,0,0,1,0,0,0,0,1]
    ebene34 = [0,0,0,1,0,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,1,0,0,0,1]
    ebene35 = [1,1,2,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,7]
    ebene36 = [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,1,1]
    ebene37 = [0,0,0,0,0,0,0,0,0,0,0,2,0,0,2,0,3,0,3,0,1]
    eben3norm = [ebene31, ebene32, ebene33, ebene34, ebene35, ebene36, ebene37]

    ebene311 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ebene312 = [0,0,3,0,0,3,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,3,0,0,0,0,0,5]
    ebene313 = [0,0,0,0,0,0,0,0,0,0,0,0,1]
    ebene314 = [0,0,0,0,0,0,0,0,0,0,0,1]
    ebene315 = [1,2,2,1,2,2,1,2,2,1,1]
    eben3under = [ebene311, ebene312, ebene313, ebene314, ebene315]

    ebene41 = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    ebene42 = [0,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    ebene51 = [0,1]
    ebene52 = [0,1,1]
    ebene53 = [0,0,1,1]
    ebene54 = [0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
    ebene55 = [0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,3,0,5,0,1,0,5]
    ebene56 = [0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0]
    ebene57 = [0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0]
    ebene58 = [0,0,0,0,0,0,0,1,8,8,8,8,9,0,0,0,0,0,8,8,8,8,8,8]



    def restart():
        global feuer
        global lastposition
        lastposition = 0
        feuer = False
        for i in range(len(blocks)-1, -1, -1):
            c.delete(blocks[i])
            del blocks[i]
        for i in range(len(lists)-1, -1, -1):
            for q in range(len(lists[i])-1, -1, -1):
                del (lists[i])[q]
        mariorichtung()


    def blau(x):
        for i in range(len(x)):
            c.itemconfig(mario[x[i]-1], fill = 'blue2', outline = 'blue2')
            colors.append(x[i]-1)
    def braun(x):
        for i in range(len(x)):
            c.itemconfig(mario[x[i]-1], fill = 'brown4', outline = 'brown4')
            colors.append(x[i]-1)
    def haut(x):
        for i in range(len(x)):
            c.itemconfig(mario[x[i]-1], fill = 'papaya whip', outline = 'papaya whip')
            colors.append(x[i]-1)
    def rot(x):
        for i in range(len(x)):
            c.itemconfig(mario[x[i]-1], fill = 'red', outline = 'red')
            colors.append(x[i]-1)
    def schwarz(x):
        for i in range(len(x)):
            c.itemconfig(mario[x[i]-1], fill = 'black', outline = 'black')
            colors.append(x[i]-1)
    def weiss(x):
        for i in range(len(x)):
            c.itemconfig(mario[x[i]-1], fill="white", outline = "white")
            colors.append(x[i]-1)
    def marionorm(x):
        global feuer
        for i in range(len(colors)-1, -1, -1):
            del colors[i]
        blau(blau1)
        braun(braun1)
        haut(haut1)
        rot(rot1)
        schwarz(schwarz1)
        himmel = 0
        if feuer == True:
            weiss(blau1)
            rot(rotfeuer)
        print(colors)
        for i in range(len(mario)):
            himmel = 0
            for q in range(len(colors)):
                if mario[i] == colors[q]+1:
                    himmel = 1
            if himmel != 1:
                if x==1:
                    c.itemconfig(mario[i], fill = "DeepSkyBlue2", outline = "DeepSkyBlue2")
                else:
                    c.itemconfig(mario[i], fill = 'black', outline = 'black')

    def mariosprung(x):
        for i in range(len(colors)-1, -1, -1):
            del colors[i]
        blau(blau2)
        braun(braun2)
        haut(haut2)
        rot(rot2)
        schwarz(schwarz2)
        himmel = 0
        #print(colors)
        if feuer == True:
            weiss(blau2)
            rot(rotfeuer2)
        for i in range(len(mario)):
            himmel = 0
            for q in range(len(colors)):
                if mario[i] == colors[q]+1:
                    himmel = 1
            if himmel != 1:
                if x==1:
                    c.itemconfig(mario[i], fill = "DeepSkyBlue2", outline = "DeepSkyBlue2")
                else:
                    c.itemconfig(mario[i], fill = 'black', outline = 'black')


    global level
    def new():
        global level
        level = 1
        ask.destroy()
    def old():
        global level
        text = open("level.txt", "r")
        for line in text:
            id1 = line.rstrip()
        level = int(id1)
        text.close()
        ask.destroy()
    def stop():
        global play
        ask.destroy()
        play = False
    ask = tk.Tk()
    c = Canvas(ask, height = 250, width = 650, bg = 'black')
    c.pack()
    for q in range(0, 16):      #Mario wird initialisiert
        for i in range(0, 16):
            id1 = c.create_rectangle(i*3.125-3.125, q*3.125-3.125, i*3.125, q*3.125, fill = 'red')
            mario.append(id1)
    for i in range(0, len(mario)):
        c.move(mario[i], 300, 25)

    B = tk.Button(ask, text="Neues Spiel", command = new)
    B.pack(side=LEFT)
    C = tk.Button(ask, text="Spielfortschritt laden", command = old)
    C.pack(side=RIGHT)
    D = tk.Button(ask, text="Spiel beenden", command=stop)
    D.pack(side=LEFT)
    mariosprung(2)
    c.create_text(325, 100, text='Super Mario Bros', font=('Lato Black', 60), fill = 'white')
    c.create_text(325, 180, text='A production of HERFARTH Enterprises in cooperation with SCHATT & Co.', font=('Lato Black', 10), fill='white')
    c.create_text(325, 200, text='Special thanks to Kohler Immobilien', font=('Lato', 10), fill='white')
    c.create_text(325, 220, text='All rights reserved', font = ('Lato Black', 10), fill='white')
    ask.update()
    ask.mainloop()
    for i in range(len(mario)-1, -1, -1):
        del mario[i]
    if play == False:
        break

    window = tk.Tk()
    window.title("Super Mario")
    c = Canvas(window, width = 2000, height = 1000, bg = "DeepSkyBlue2")
    c.pack()
    for q in range(0, 16):      #Mario wird initialisiert
        for i in range(0, 16):
            id1 = c.create_rectangle(i*3.125-3.125, q*3.125-3.125, i*3.125, q*3.125, fill = 'red')
            mario.append(id1)
    for i in range(0, len(mario)):
        c.move(mario[i], 200, 552)
        window.update()



    def mariounder():
        for i in range(len(mario)):
            himmel = 0
            for q in range(len(colors)):
                if mario[i] == colors[q]+1:
                    himmel = 1
            if himmel != 1:
                c.itemconfig(mario[i], fill = 'black', outline = 'black')

    def mariorueckwaerts(x):
        for i in range(len(colors)-1,-1,-1):
            del colors[i]
        rot(rot3)
        blau(blau3)
        braun(braun3)
        haut(haut3)
        schwarz(schwarz3)
        himmel = 0
        if feuer == True:

            weiss(blau3)
            rot(rotfeuer3)
        for i in range(len(mario)):
             himmel = 0
             for q in range(len(colors)):
                 if mario[i] == colors[q]+1:
                     himmel = 1
             if himmel != 1:
                 if x==1:
                     c.itemconfig(mario[i], fill = "DeepSkyBlue2", outline = "DeepSkyBlue2")
                 else:
                     c.itemconfig(mario[i], fill = 'black', outline = 'black')

    def mariosprungrueckwaerts(x):
        global feuer
        for i in range(len(colors)-1,-1,-1):
             del colors[i]
        blau(blau4)
        schwarz(schwarz4)
        rot(rot4)
        haut(haut4)
        braun(braun4)
        if feuer == True:
            weiss(blau4)
            rot(rotfeuer4)
        for i in range(len(mario)):
             himmel = 0
             for q in range(len(colors)):
                 if mario[i] == colors[q]+1:
                     himmel = 1
             if himmel != 1:
                 if x==1:
                     c.itemconfig(mario[i], fill = "DeepSkyBlue2", outline = "DeepSkyBlue2")
                 else:
                     c.itemconfig(mario[i], fill = 'black', outline = 'black')

    def mariorichtung():
        global move
        global underground
        if underground == False:
            x = 1
        else:
            x = 3
        if move == True:
            marionorm(x)
        else:
            mariorueckwaerts(x)

    def mariosprungrichtung():
        global move
        global underground
        if underground == False:
            x = 1
        else:
            x = 3
        if move == True:
            mariosprung(x)
        else:
            mariosprungrueckwaerts(x)
    def weissBowser(x):
        for i in range(len(x)):
            c.itemconfig(bowser[x[i]-1], fill="white", outline = "white")
            bowsercolors.append(bowser[x[i]-1])
    def gruenBowser(x):
        for i in range(len(x)):
            c.itemconfig(bowser[x[i]-1], fill="green2", outline = "green2")
            bowsercolors.append(bowser[x[i]-1])
    def schwarzBowser(x):
        for i in range(len(x)):
            c.itemconfig(bowser[x[i]-1], fill="black", outline = "black")
            bowsercolors.append(bowser[x[i]-1])
    def orangeBowser(x):
        for i in range(len(x)):
            c.itemconfig(bowser[x[i]-1], fill="orange", outline = "orange")
            bowsercolors.append(bowser[x[i]-1])
    def orangeBowserFeuer(x):
        for i in range(len(x)):
            c.itemconfig(zwischenbowserfeuer[x[i]-1], fill="gold", outline = "gold")
            bowserfeuercolor.append(zwischenbowserfeuer[x[i]])
    def rotBowserFeuer(x):
        for i in range(len(x)):
            c.itemconfig(zwischenbowserfeuer[x[i]-1], fill="red", outline ="red")
            bowserfeuercolor.append(zwischenbowserfeuer[x[i]])
    def weissBowserFeuer(x):
        for i in range(len(x)):
            c.itemconfig(zwischenbowserfeuer[x[i]], fill="white", outline="white")
            bowserfeuercolor.append(zwischenbowserfeuer[x[i]])
    def bowserfeuer1():
        for i in range(len(zwischenbowserfeuer)-1, -1, -1):
            del zwischenbowserfeuer[i]
        for i in range(len(bowserfeuercolor)-1, -1, -1):
            del bowserfeuercolor[i]
        for q in range(0, 17):      #Mario wird initialisiert
            for i in range(0, 16):
                id1 = c.create_rectangle(i*3.125-3.125, q*3.125-3.125, i*3.125, q*3.125, fill = 'red', outline = 'red')
                bowserfeuer.append(id1)
                zwischenbowserfeuer.append(id1)
                blocks.append(id1)
        x, y = hole_koord(bowser[500])
        x1, y1 = hole_koord(zwischenbowserfeuer[0])
        for i in range(len(zwischenbowserfeuer)):
            c.move(zwischenbowserfeuer[i],x-x1-50,y-y1)
        rotBowserFeuer(bowserFeuerRot)
        rotBowserFeuer(bowserFeuerRot2)
        rotBowserFeuer(bowserFeuerRot3)
        orangeBowserFeuer(bowserOrangeFeuer)
        weissBowserFeuer(bowserFeuerWeiss)
        for i in range(len(zwischenbowserfeuer)):
            himmel = 0
            for q in range(1, len(bowserfeuercolor)-1):
                if zwischenbowserfeuer[i] == bowserfeuercolor[q+1]:
                    himmel = 1
            if himmel != 1:
                c.itemconfig(zwischenbowserfeuer[i], fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
    def bowsernorm(x):
        for i in range(len(bowsercolors)-1,-1,-1):
            del bowsercolors[i]
        weissBowser(bowserWeiss)
        weissBowser(bowserWeiss2)
        weissBowser(bowserWeiss3)
        weissBowser(bowserWeiss4)
        schwarzBowser(bowserSchwarz)
        orangeBowser(bowserOrange)
        orangeBowser(bowserOrange2)
        orangeBowser(bowserOrange3)
        gruenBowser(bowserGruen)
        gruenBowser(bowserGruen2)
        gruenBowser(bowserGruen3)
        gruenBowser(bowserGruen4)
        gruenBowser(bowserGruen5)
        for i in range(len(bowser)):
            himmel = 0
            for q in range(len(bowsercolors)):
                if bowser[i] == bowsercolors[q]:
                    himmel = 1
            if himmel != 1:
                c.itemconfig(bowser[i], fill = "DeepSkyBlue2", outline = "DeepSkyBlue2")
    def hole_koord(id_num):

        pos = c.coords(id_num)
        x = (pos[0] + pos[2])/2
        y = (pos[1] + pos[3])/2
        return x, y


    def distanz(id1, id2):
        x1, y1 = hole_koord(id1)
        x2, y2 = hole_koord(id2)
        return sqrt((x2 -x1) ** 2 + (y2 - y1) ** 2)

    def ebeninit(x):
        global underground
        if x == 1:
            for i in range(1, 21):
                id1 = c.create_rectangle(i*50 - 50, 1000, i * 50, 625, fill = 'DarkOrange4', outline='DarkOrange4')
                id2 = c.create_rectangle(i*50-50, 650, i*50, 600, fill = 'green4', outline='green4')
                id3 = c.create_oval(i*50-50, 650, i*50, 600, fill = 'green4', outline='green4')
                blocks.append(id3)
                blocks.append(id1)
                blocks.append(id2)
                falllist.append(id3)
                for q in range(1, 6):
                    id4 = c.create_rectangle(i*50+q*10-60, 610,i*50+q*10-50, 600, fill = 'green4', outline='green4')
                    blocks.append(id4)
                    falllist.append(id4)
        else:
            for i in range(1, 21):
                id1 = c.create_rectangle(i*50 - 50, 1000, i * 50, 625, fill = 'LightSteelBlue4', outline='LightSteelBlue4')
                id2 = c.create_rectangle(i*50-50, 650, i*50, 600, fill = 'LightSteelBlue3', outline='LightSteelBlue3')
                id3 = c.create_oval(i*50-50, 650, i*50, 600, fill = 'LightSteelBlue3', outline='LightSteelBlue3')
                blocks.append(id3)
                blocks.append(id1)
                blocks.append(id2)
                falllist.append(id3)
                for q in range(1, 6):
                    id4 = c.create_rectangle(i*50+q*10-60, 610,i*50+q*10-50, 600, fill = 'LightSteelBlue3', outline='LightSteelBlue3')
                    blocks.append(id4)
                    falllist.append(id4)
    def eben1(x, y):
        global underground
        for i in range(1, len(x)):
            if x[i] == 1:
                if y == 1:
                    id1 = c.create_rectangle(1000 + i*50-50, 1000, 1000+i*50, 625, fill = 'DarkOrange4', outline='DarkOrange4')
                    id2 = c.create_rectangle(1000+i*50-50, 650,1000 + i*50, 600, fill = 'green4', outline='green4')
                    for q in range(1, 6):
                            id4 = c.create_rectangle(1000+i*50+q*10-60, 610,1000+i*50+q*10-50, 600, fill = 'green4', outline='green4')
                            blocks.append(id4)
                            falllist.append(id4)
                else:
                    id1 = c.create_rectangle(1000 + i*50-50, 1000, 1000+i*50, 625, fill = 'LightSteelBlue4', outline= 'LightSteelBlue4')
                    id2 = c.create_rectangle(1000+i*50-50, 650,1000 + i*50, 600, fill = 'LightSteelBlue3', outline='LightSteelBlue3')
                    for q in range(1, 6):
                            id4 = c.create_rectangle(1000+i*50+q*10-60, 610,1000+i*50+q*10-50, 600, fill = 'LightSteelBlue3', outline='LightSteelBlue3')
                            blocks.append(id4)
                            falllist.append(id4)
                blocks.append(id1)
                blocks.append(id2)
                window.update()
    def mariomove(x, y):
        for i in range(len(mario)):
            c.move(mario[i], x, y)
    def ebene(x, y, p):
        global goodflag
        global underground
        print(p)
        for i in range(len(x)):
            if x[i] == 1:
                for q in range(1, 7):
                    if q == 6:
                        if p == 0:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                            #print("Norm")
                        else:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'black', outline = 'black')
                            #print("Exception")
                    else:
                        id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'grey', outline = 'grey')
                    blocks.append(id1)
                    falllist.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-50, y-60+q*10, 1000+i*50-40, y-50+q*10, outline = 'grey')
                    id2 = c.create_rectangle(1000+i*50-40, y-60+q*10, 1000+i*50-30, y-50 + q*10, outline = 'grey')
                    blocks.append(id2)
                    links.append(id2)
                    blocks.append(id1)
                    links.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-10, y-60+q*10, 1000+i*50, y-50+q*10, outline='grey')
                    id2 = c.create_rectangle(1000+i*50-20, y-60+q*10, 1000+i*50, y-50+q*10, outline = 'grey')
                    blocks.append(id2)
                    rechts.append(id2)
                    blocks.append(id1)
                    rechts.append(id1)
                if p == 0:
                    id2 = c.create_rectangle(1000+i*50-50, y,1000 + i*50, y-50, fill = 'OrangeRed4', outline='OrangeRed4')
                else:
                    id2 = c.create_rectangle(1000+i*50-50, y,1000 + i*50, y-50, fill = 'LightSteelBlue3', outline='LightSteelBlue3')
                id3 = c.create_rectangle(1000+i*50-50,y,1000+i*50,y-3,fill="black")
                id4 = c.create_rectangle(1000+i*50-40,y,1000+i*50-37,y-13,fill="black")
                id5 = c.create_rectangle(1000+i*50-10,y,1000+i*50-7,y-13,fill="black")
                id6 = c.create_rectangle(1000+i*50-50,y-13,1000+i*50,y-16,fill="black")
                id7 = c.create_rectangle(1000+i*50-27,y-16,1000+i*50-24,y-27,fill="black")
                id8 = c.create_rectangle(1000+i*50-50,y-27,1000+i*50,y-30,fill="black")
                id9 = c.create_rectangle(1000+i*50-4,y-16,1000+i*50,y-27,fill="black")
                id10 = c.create_rectangle(1000+i*50-40,y-30,1000+i*50-37,y-43,fill="black")
                id11 = c.create_rectangle(1000+i*50-10,y-30,1000+i*50-7,y-43,fill="black")
                id12 = c.create_rectangle(1000+i*50,y-41,1000+i*50-50,y-44,fill="black")
                sprunglist.append(id2)
                blocks.append(id2)
                blocks.append(id3)
                blocks.append(id4)
                blocks.append(id5)
                blocks.append(id6)
                blocks.append(id7)
                blocks.append(id8)
                blocks.append(id9)
                blocks.append(id10)
                blocks.append(id11)
                blocks.append(id12)

            elif x[i] == 2:
                id4 = c.create_oval(1000+i*50-50, y, 1000+i*50, y-25, fill='purple', outline = 'purple')
                for q in range(1, 7):
                    if q ==6:
                        if p == 0:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                        else:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'black', outline = 'black')
                    else:
                        id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'purple', outline = 'purple')
                    blocks.append(id1)
                    falllist.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-50, y-60+q*10, 1000+i*50-40, y-50+q*10, outline='purple')
                    blocks.append(id1)
                    links.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-10, y-60+q*10, 1000+i*50, y-50+q*10, outline = 'purple')
                    blocks.append(id1)
                    rechts.append(id1)
                id2 = c.create_rectangle(1000+i*50-50, y-3,1000 + i*50, y-50, fill = 'sienna1', outline='sienna1')
                id3 = c.create_rectangle(1000+i*50-35,y-35,1000+i*50-30,y-25,fill="DarkOrange3",outline="DarkOrange3")
                id5 = c.create_rectangle(1000+i*50-30,y-35,1000+i*50-20,y-38,fill="DarkOrange3",outline="DarkOrange3")
                id6 = c.create_rectangle(1000+i*50-20,y-35,1000+i*50-16,y-23,fill="DarkOrange3",outline="DarkOrange3")
                id7 = c.create_rectangle(1000+i*50-20,y-23,1000+i*50-24,y-19,fill="DarkOrange3",outline="DarkOrange3")
                id8 = c.create_rectangle(1000+i*50-20,y-14,1000+i*50-24,y-10,fill="DarkOrange3",outline="DarkOrange3")
                id9 = c.create_rectangle(1000+i*50-3,y,1000+i*50,y-50,fill="black")
                id10 = c.create_rectangle(1000+i*50-50,y-3,1000+i*50,y,fill="black")
                id11 = c.create_rectangle(1000+i*50-13,y-5,1000+i*50-9,y-9,fill="black")
                id12 = c.create_rectangle(1000+i*50-13,y-45,1000+i*50-9,y-41,fill="black")
                id13 = c.create_rectangle(1000+i*50-39,y-45,1000+i*50-43,y-41,fill="black")
                id14 = c.create_rectangle(1000+i*50-39,y-5,1000+i*50-43,y-9,fill="black")
                blocks.append(id2)
                blocks.append(id3)
                blocks.append(id4)
                blocks.append(id5)
                blocks.append(id6)
                blocks.append(id7)
                blocks.append(id8)
                blocks.append(id9)
                blocks.append(id10)
                blocks.append(id11)
                blocks.append(id12)
                blocks.append(id13)
                blocks.append(id14)
                boni.append(id4)
                boni2.append(id2)
                boni3.append(id2)
                sprunglist.append(id2)
            elif x[i] == 3:
                if p == 0:
                    id1 = c.create_rectangle(1000+i*50-50, y, 1000+i*50, y-50, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                    id2 = c.create_oval(1000+i*50-50, y-25, 1000+i*50, y-50, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                    id3 = c.create_oval(1000+i*50-50, y, 1000+i*50-25, y-50, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                    id4 = c.create_oval(1000+i*50-25, y, 1000+i*50, y-50, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                else:
                    id1 = c.create_rectangle(1000+i*50-50, y, 1000+i*50, y-50, fill = 'black', outline = 'black')
                    id2 = c.create_oval(1000+i*50-50, y-25, 1000+i*50, y-50, fill = 'black', outline = 'black')
                    id3 = c.create_oval(1000+i*50-50, y, 1000+i*50-25, y-50, fill = 'black', outline = 'black')
                    id4 = c.create_oval(1000+i*50-25, y, 1000+i*50, y-50, fill = 'black', outline = 'black')
                for q in range(0, 7):
                    for f in range(0, 6):
                        if p == 0:
                            id5 = c.create_rectangle(1010+i*50+f*25/3-(50+25/3), y+q*6-36, 1010+i*50+f*25/3-(50), y+q*6-42, fill='DeepSkyBlue2', outline = 'DeepSkyBlue2')
                        else:
                            id5 = c.create_rectangle(1010+i*50+f*25/3-(50+25/3), y+q*6-36, 1010+i*50+f*25/3-(50), y+q*6-42, fill='black', outline = 'black')
                        baddesign.append(id5)
                        blocks.append(id5)
                        zwischendesign.append(id5)
                for z in range(len(badbraun)):
                    c.itemconfig(zwischendesign[badbraun[z]], fill = 'burlywood4', outline = 'burlywood4')
                for z in range(len(badschwarz)):
                    c.itemconfig(zwischendesign[badschwarz[z]], fill = 'black', outline = 'black')
                for z in range(len(zwischendesign)-1, -1, -1):
                    del zwischendesign[z]
                blocks.append(id1)
                blocks.append(id2)
                blocks.append(id3)
                blocks.append(id4)
                badlist.append(id1)
                badlistlinks.append(id3)
                badlistrechts.append(id4)
                badlistoben.append(id2)
            elif x[i] == 4:
                for q in range(1, 7):
                    if q == 6:
                        if p == 0:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                            #print("Norm")
                        else:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'black', outline = 'black')
                            #print("Exception")
                    else:
                        id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'grey', outline = 'grey')
                    blocks.append(id1)
                    falllist.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-50, y-60+q*10, 1000+i*50-40, y-50+q*10, outline = 'grey')
                    blocks.append(id1)
                    links.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-10, y-60+q*10, 1000+i*50, y-50+q*10, outline='grey')
                    blocks.append(id1)
                    rechts.append(id1)
                id1 = c.create_polygon(1000+i*50-50, y-225, 1000+i*50, y-200, 1000+i*50, y-250, fill = 'white')
                id4 = c.create_polygon(1000+i*50-50, y-25, 1000+i*50, y, 1000+i*50, y-50, fill='red')
                id2 = c.create_rectangle(1000+i*50-1, y-200, 1000+i*50, y, fill = 'black')
                id3 = c.create_rectangle(1000+i*50-50, y-50, 1000+i*50, y, fill = 'black')
                blocks.append(id1)
                blocks.append(id2)
                blocks.append(id3)
                flag.append(id1)
                goodflag = id4
                blocks.append(id4)
            elif x[i] == 5:
               for q in range(1, 8):
                    if q == 7 or q == 1:
                        id1 = c.create_rectangle(1000+i*50+q*10-70, y-50,1000+i*50+q*10-60, y-40, fill = 'green', outline = 'green')
                    else:
                        id1 = c.create_rectangle(1000+i*50+q*10-70, y-50,1000+i*50+q*10-60, y-40, fill = 'grey', outline = 'grey')
                    blocks.append(id1)
                    falllist.append(id1)
                    switch.append(id1)
               for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-50, y-60+q*10, 1000+i*50-40, y-50+q*10, outline = 'grey')
                    blocks.append(id1)
                    links.append(id1)
               for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-10, y-60+q*10, 1000+i*50, y-50+q*10, outline='grey')
                    blocks.append(id1)
                    rechts.append(id1)
               id2 = c.create_rectangle(1000+i*50-50, y,1000 + i*50, y-50, fill = 'green', outline='green')
               blocks.append(id2)
            elif x[i] == 6:
                #Bowser wird initialisiert
                for q in range(0,32):
                    for f in range(0,32):
                        id1 = c.create_rectangle(f*3.125-3.125, q*3.125-3.125, f*3.125, q*3.125, fill = 'red')
                        bowser.append(id1)
                        blocks.append(id1)
                        if q == 0:
                            bowserkill.append(id1)
                for f in range(0, len(bowser)):
                        c.move(bowser[f], 1000+i*50,1100-y)
                bowsernorm(1)
            elif x[i] == 7:
                id4 = c.create_oval(1000+i*50-50, y, 1000+i*50, y-25, fill='purple', outline = 'purple')
                id5 = c.create_rectangle(1000+i*50-50, y, 1000+i*50, y-50, fill='black')
                for q in range(1, 7):
                    if q ==6:
                        if p == 0:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                        else:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'black', outline = 'black')
                    else:
                        id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'purple', outline = 'purple')
                    blocks.append(id1)
                    falllist.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-50, y-60+q*10, 1000+i*50-40, y-50+q*10, outline='purple')
                    blocks.append(id1)
                    links.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-10, y-60+q*10, 1000+i*50, y-50+q*10, outline = 'purple')
                    blocks.append(id1)
                    rechts.append(id1)
                buylist.append(id4)
                blocks.append(id4)
                blocks.append(id5)
            elif x[i] == 8:
                for q in range(1, 7):
                    if q ==6:
                        if p == 0:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                        else:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                    else:
                        id1 = c.create_rectangle(1000+i*50+q*10-58, y-49,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                    blocks.append(id1)
                    falllist.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-50, y-60+q*10, 1000+i*50-40, y-50+q*10, outline='DeepSkyBlue2')
                    blocks.append(id1)
                    links.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-10, y-60+q*10, 1000+i*50, y-50+q*10, outline = 'DeepSkyBlue2')
                    blocks.append(id1)
                id1 = c.create_rectangle(1000+i*50-40,y-10,1000+i*50-10,y-40, fill="white",outline="white")
                id2 = c.create_oval(1000+i*50-50,y-50,1000+i*50-40,y-40,fill="white",outline="white")
                id3 = c.create_rectangle(1000+i*50-50,y-5,1000+i*50-40,y-45,fill="white",outline="white")
                id4 = c.create_oval(1000+i*50-50,y-1,1000+i*50-40,y-10,fill="white",outline="white")
                id5 = c.create_rectangle(1000+i*50-45,y,1000+i*50-5,y-10,fill="white",outline="white")
                id6 = c.create_oval(1000+i*50,y,1000+i*50-10,y-10,fill="white",outline="white")
                id7 = c.create_rectangle(1000+i*50,y-5,1000+i*50-10,y-45,fill="white",outline="white")
                id8 = c.create_oval(1000+i*50,y-40,1000+i*50-10,y-50,fill="white",outline="white")
                id9 = c.create_rectangle(1000+i*50-6,y-50,1000+i*50-44,y-40,fill="white",outline="white")
                id10 = c.create_oval(1000+i*50-40,y-20,1000+i*50-35,y-45,fill="black",outline="black")
                id11 = c.create_oval(1000+i*50-10,y-20,1000+i*50-15,y-45,fill="black",outline="black")
                falllist.append(id1)
                blocks.append(id1)
                blocks.append(id2)
                blocks.append(id3)
                blocks.append(id4)
                blocks.append(id5)
                blocks.append(id6)
                blocks.append(id7)
                blocks.append(id8)
                blocks.append(id9)
                blocks.append(id10)
                blocks.append(id11)
            elif x[i] == 9:
                for q in range(1, 7):
                    if q ==6:
                        if p == 0:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                        else:
                            id1 = c.create_rectangle(1000+i*50+q*10-60, y-50,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                    else:
                        id1 = c.create_rectangle(1000+i*50+q*10-58, y-49,1000+i*50+q*10-50, y-40, fill = 'DeepSkyBlue2', outline = 'DeepSkyBlue2')
                    blocks.append(id1)
                    falllist.append(id1)
                    plattform.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-50, y-60+q*10, 1000+i*50-40, y-50+q*10, outline='DeepSkyBlue2')
                    blocks.append(id1)
                    links.append(id1)
                    plattform.append(id1)
                for q in range(1, 6):
                    id1 = c.create_rectangle(1000+i*50-10, y-60+q*10, 1000+i*50, y-50+q*10, outline = 'DeepSkyBlue2')
                    blocks.append(id1)
                    plattform.append(id1)
                id1 = c.create_oval(1000+i*50-50,y-40,1000+i*50-40,y-50,fill="red2",outline="red2")
                id2 = c.create_rectangle(1000+i*50-45,y-40,1000+i*50-5,y-50,fill="red2",outline="red2")
                id3 = c.create_oval(1000+i*50-10,y-40,1000+i*50,y-50,fill="red2",outline="red2")
                blocks.append(id1)
                plattform.append(id1)
                blocks.append(id2)
                plattform.append(id2)
                blocks.append(id3)
                plattform.append(id3)
    def gegensteuerung():
        global lastposition
        global speed
        for i in range(len(sprunglist)):
            if distanz(mario[8], sprunglist[i]) < 23 or distanz(mario[0], sprunglist[i]) < 10 or distanz(mario[15], sprunglist[i]) < 10:
               mariomove(0, 25)
        for i in range(len(links)):
            if distanz(mario[143], links[i]) < 6:
                for i in range(len(blocks)):
                    c.move(blocks[i], speed, 0)
                print("GEEEEEEEEEEEEEEGEN")
                lastposition += -1
        for i in range(len(rechts)):
            if distanz(mario[145], rechts[i]) < 6:
                for i in range(len(blocks)):
                    c.move(blocks[i], -speed, 0)
                lastposition += 1


    def enemy():
        global badcounter
        global badrichtung
        global leben
        global points
        global badspeed
        badcounter += 1
        if badcounter == 15:
            badcounter = 0
            badrichtung = badrichtung*-1
        for i in range(len(badlist)):
            c.move(badlist[i], badspeed*badrichtung, 0)
            c.move(badlistrechts[i], badspeed*badrichtung, 0)
            c.move(badlistlinks[i],badspeed*badrichtung, 0)
            c.move(badlistoben[i], badspeed*badrichtung, 0)
        for i in range(len(baddesign)):
            c.move(baddesign[i], badspeed*badrichtung, 0)
        for i in range(len(badlistlinks)):
            if distanz(mario[143], badlistlinks[i]) < 10:
                levelminus()
        for i in range(len(badlistrechts)):
            if distanz(mario[144], badlistrechts[i]) < 10:
                levelminus()
        for i in range(len(badlistoben)-1, -1, -1):
            if distanz(mario[247], badlistoben[i]) < 30:
                c.delete(badlist[i])
                del badlist[i]
                c.delete(badlistrechts[i])
                del badlistrechts[i]
                c.delete(badlistlinks[i])
                del badlistlinks[i]
                c.delete(badlistoben[i])
                del badlistoben[i]
                for z in range(0, 42):
                    c.delete(baddesign[i*42])
                    del baddesign[i*42]
                points += 1000
        for i in range(len(balls)):
            for q in range(len(balls[i])):
                for f in range(len(badlist)-1, -1, -1):
                    if distanz(balls[i][q], badlist[f]) < 10:
                        c.delete(badlist[f])
                        del badlist[f]
                        c.delete(badlistrechts[f])
                        del badlistrechts[f]
                        c.delete(badlistlinks[f])
                        del badlistlinks[f]
                        c.delete(badlistoben[f])
                        del badlistoben[f]
                        for z in range(0, 42):
                            c.delete(baddesign[f*42])
                            del baddesign[f*42]
                        points += 1000

                #pygame.mixer.music.pause()
                #pygame.mixer.Sound.play(killsound)



    def bowserfunc():
        global badfeuerschonzeit
        global leben
        if len(bowser) > 0:
            badfeuerschonzeit += -1
            if badfeuerschonzeit < 0:
                if distanz(bowser[0], mario[0]) < 7000:
                    bowserfeuer1()
                    badfeuerschonzeit = 40
            for i in range(len(bowserfeuer)):
                c.move(bowserfeuer[i], -10, 0)
                if distanz(bowserfeuer[i], mario[75]) < 5:
                    levelminus()
            for i in range(0,31):
                if distanz(mario[247], bowserkill[i]) < 7:
                    for q in range(len(bowser)-1, -1, -1):
                        c.delete(bowser[q])
                        del bowser[q]
                    for q in range(len(bowserfeuer)):
                        c.delete(bowserfeuer[q])
                break
            for i in range(len(bowser)):
                if distanz(mario[8], bowser[i]) < 5:
                    leben += -100
    def under(x, y, z):
        global underground
        global undergroundlevel
        global lastposition
        global underposition
        global speed
        for i in range(len(switch)):
            if distanz(mario[247], switch[i]) < 20:
                if underground == False:
                    if undergroundlevel == x:
                        underground = True
                        underposition = lastposition
                        lastposition = 0
                        undergroundlevel += 1
                        sleep(0.3)
                        mariounder()
                        restart()
                        c.configure(background="black")
                        c.itemconfig(punkttext, fill = 'white')
                        ebeninit(2)
                        for q in range(len(y)):
                            if q == 0:
                                eben1(y[q], 2)
                            else:
                                ebene(y[q], 650-q*50, 2)
                        mariorichtung()
                    break
                if underground == True:
                    if undergroundlevel == x+1:
                        undergroundlevel += 1
                        underground = False
                        restart()
                        ebeninit(1)
                        for q in range(len(z)):
                            if q == 0:
                                eben1(z[q], 1)
                            else:
                                ebene(z[q], 650-q*50, 0)
                        distance = underposition*speed + 100
                        for q in range(len(blocks)):
                            c.move(blocks[q], -distance, 0)
                        mariorichtung()
                        underposition = 0
                        lastposition = 0
                        c.configure(background="DeepSkyBlue2")
                        c.itemconfig(punkttext, fill = 'black')

    def bonus():
        for i in range(len(boni)-1, -1, -1):
            if distanz(mario[8], boni[i]) < 25:
                x, y= hole_koord(boni[i])
                c.itemconfig(boni[i], fill = 'grey', outline = 'grey')
                c.itemconfig(boni2[i], fill = 'grey', outline = 'grey')
                c.itemconfig(boni3[i], fill = 'grey', outline = 'grey')
                del boni[i]
                del boni2[i]
                del boni3[i]
              #  pygame.mixer.Sound.play(mysterysound)
               # if randint(1, 5) == 1:
                  #  id1 = c.create_rectangle(
                if randint(1,4) == 1:
                    tupel = []
                    id6 = c.create_rectangle(x-2,y-55,x+2,y-37,fill="green",outline="green")
                    id1 = c.create_oval(x-30, y-55, x+30, y-95, fill = 'red')
                    id2 = c.create_oval(x-25, y-60, x+25, y-90, fill = 'yellow',outline="yellow")
                    id3 = c.create_oval(x-20, y-65, x+20, y-85, fill="white")
                    id4 = c.create_oval(x-10,y-70,x-6,y-80, fill="black")
                    id5 = c.create_oval(x+10,y-70,x+6,y-80,fill="black")
                    id7 = c.create_oval(x-35,y-55,x-2,y-40,fill="green",outline="green")
                    id8 = c.create_oval(x+2,y-55,x+35,y-40,fill="green",outline="green")
                    blocks.append(id1)
                    blocks.append(id2)
                    blocks.append(id3)
                    blocks.append(id4)
                    blocks.append(id5)
                    blocks.append(id6)
                    blocks.append(id7)
                    blocks.append(id8)
                    tupel.append(id1)
                    tupel.append(id2)
                    tupel.append(id3)
                    tupel.append(id4)
                    tupel.append(id5)
                    tupel.append(id6)
                    tupel.append(id7)
                    tupel.append(id8)
                    feuerlist.append(tupel)
                elif randint(1, 15) == 1:
                        tupel = []
                        id1 = c.create_rectangle(x-20,y-78,x+20,y-90,fill="red",outline="red")
                        id2 = c.create_rectangle(x-15,y-95,x-3,y-73,fill="red",outline="red")
                        id3 = c.create_rectangle(x+15,y-95,x+3,y-73,fill="red",outline="red" )
                        id4 = c.create_rectangle(x+10,y-78,x-10,y-68,fill="red",outline="red")
                        id5 = c.create_rectangle(x+5,y-69,x-5,y-63,fill="red",outline="red")
                        blocks.append(id1)
                        blocks.append(id2)
                        blocks.append(id3)
                        blocks.append(id4)
                        blocks.append(id5)
                        tupel.append(id1)
                        tupel.append(id2)
                        tupel.append(id3)
                        tupel.append(id4)
                        tupel.append(id5)
                        hearts.append(tupel)
                        print("HHhearrrrrttttssssssssssssssssssss")
                        print(hearts)
                else:
                    if randint(1, 2) == 1:
                        id1 = c.create_oval(x-20, y-50, x+20, y-90, fill = 'DarkGoldenrod4')
                        id2 = c.create_oval(x-17, y-53, x+17, y-87, fill = 'gold2', outline = 'black')
                        goldlist.append(id2)
                        blocks.append(id2)
                        goldlist2.append(id1)
                        blocks.append(id1)
                    else:
                        id1 = c.create_oval(x-20, y-50, x+20, y-90, fill = 'seashell4')
                        id2 = c.create_oval(x-17, y-53, x+17, y-87, fill = 'seashell3', outline = 'black')
                        silberlist.append(id2)
                        blocks.append(id2)
                        silberlist2.append(id1)
                        blocks.append(id1)
    def kaufen():
        global points
        global leben
        if points > 15000:
            for i in range(len(buylist)):
                if distanz(mario[8], buylist[i]) < 70:
                    leben += 1
                    points += -15000
    def punkte():
        global points
        global feuer
        global leben
        heart = False
        for i in range(len(goldlist)-1, -1, -1):
            if distanz(mario[126], goldlist[i]) < 30:
                c.delete(goldlist[i])
                del goldlist[i]
                c.delete(goldlist2[i])
                del goldlist2[i]
                points += 800
                print(points)
               #pygame.mixer.Sound.play(bonussound)
        for i in range(len(silberlist)-1, -1, -1):
            if distanz(mario[126], silberlist[i]) < 30:
                c.delete(silberlist[i])
                del silberlist[i]
                c.delete(silberlist2[i])
                del silberlist2[i]
                points += 400
                print(points)
                #pygame.mixer.music.pause()
               # pygame.mixer.Sound.play(bonussound)
        for i in range(len(feuerlist)-1, -1, -1):
            if feuer != True:
                for q in range(len(feuerlist[i])-1, -1, -1):
                    if feuer != True:
                        if distanz(mario[126], feuerlist[i][q]) < 30:
                            for f in range(len(feuerlist[i])-1, -1, -1):
                                c.delete(feuerlist[i][f])
                                del feuerlist[i][f]
                            del feuerlist[i]
                            print("FEUERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR!")
                            feuer = True
        for i in range(len(hearts)-1, -1, -1):
            if heart != True:
                for q in range(len(hearts[i])-1, -1, -1):
                    if heart != True:
                        if distanz(mario[126], hearts[i][q]) < 30:
                            for f in range(len(hearts[i])-1, -1, -1):
                                c.delete(hearts[i][f])
                                del hearts[i][f]
                            del hearts[i]
                            heart = True
                            leben += 1
                            break


    def movement(event):
        global sprungerlaubnis
        global height
        global rundenzahl
        global bewegungserlaubnis
        global rechts2
        global links2
        global feuerschonzeit
        global move
        global feuerrichtungnormal
        if bewegungserlaubnis == True:
            if event.keysym == 'Right':
                rechts2 = True
                links2 = False
                move = True
                feuerrichtungnormal = True
                if height == 1:
                    mariosprungrichtung()
                else:
                    mariorichtung()
            elif event.keysym == 'Left':
                links2 = True
                rechts2 = False
                move = False
                feuerrichtungnormal = False
                if height == 1:
                    mariosprungrichtung()
                else:
                    mariorichtung()
            elif event.keysym == 'Up':
                if height == 0:
                    if sprungerlaubnis == 0:
                        mariosprungrichtung()
                        for i in range(1, 5):
                            mariomove(0, -25)
                            gegensteuerung()
                        bonus()
                        rundenzahl = 0
                        height = 1
                        sprungerlaubnis = 1
            elif event.keysym == 's':
                if feuer == True:
                    if feuerschonzeit < 1:
                        x, y = hole_koord(mario[126])
                        tupel = []
                        id1 = c.create_oval(x+5, y+5, x-5, y-5, fill = 'red')
                        id2 = c.create_oval(x+3, y+3, x-3, y-3, fill = 'orange')
                        tupel.append(id1)
                        tupel.append(id2)
                        blocks.append(id1)
                        blocks.append(id2)
                        if feuerrichtungnormal==True:
                            balls.append(tupel)
                        else:
                            balls2.append(tupel)
                        feuerschonzeit = 5
            else:
                links2 = False
                rechts2 = False
            window.update()
    c.bind_all('<Key>', movement)

    def feuermod():
        global feuerschonzeit
        destroy = False
        feuerschonzeit += -1
        for i in range(len(balls)-1, -1, -1):
            if destroy == True:
                break
            for q in range(len(balls[i])-1, -1, -1):
                if destroy == True:
                    break
                c.move(balls[i][q], 25, 0)
                for f in range(len(links)):
                    if distanz(balls[i][q], links[f]) < 15:
                        for z in range(len(balls[i])-1, -1, -1):
                            c.delete(balls[i][z])
                            del balls[i][z]
                        del balls[i]
                        destroy = True
                        break
        destroy = False
        for i in range(len(balls2)-1, -1, -1):
            if destroy == True:
                break
            for q in range(len(balls2[i])-1, -1, -1):
                if destroy == True:
                    break
                c.move(balls2[i][q], -25, 0)
                for f in range(len(rechts)):
                    if distanz(balls2[i][q], rechts[f]) < 15:
                        for z in range(len(balls2[i])-1, -1, -1):
                            c.delete(balls2[i][z])
                            del balls2[i][z]
                        del balls2[i]
                        destroy = True
                        break

    def bewegung():
        global rechts2
        global links2
        global lastposition
        global speed
        if rechts2 == True:
            for i in range(len(blocks)):
                c.move(blocks[i], -speed, 0)
            lastposition += 1
        if links2 == True:
            for i in range(len(blocks)):
                c.move(blocks[i], speed, 0)
            lastposition += -1

    def sprung():
        global rundenzahl
        global sprungerlaubnis
        global height
        if sprungerlaubnis == 1:
                rundenzahl = rundenzahl + 1
                print(rundenzahl)
                if rundenzahl == 10:
                    height = 0
                    mariorichtung()
                    anzahl = 0
                    for i in range(1, 10):
                        for i in range(len(falllist)):
                            if distanz(mario[248], falllist[i]) < 10 or distanz(mario[255], falllist[i]) < 7 or distanz(mario[240], falllist[i]) < 9:
                                anzahl = 1
                        if anzahl != 1:
                            mariomove(0, (25/3) * 2)
                            gegensteuerung()
                            enemy()
                            print("Runteer")
                        window.update()
                if rundenzahl == 11:
                    sprungerlaubnis = 0


    def sturz():
        global höhe
        global leben
        safe = 1
        global bewegungserlaubnis
        if height == 0:
            for i in range(1, len(falllist)):
                if distanz(mario[248], falllist[i]) < 15:
                    safe = 0
                    bewegungserlaubnis = True
            if safe != 0:
                for i in range(1, 3):
                    if safe != 0:
                        mariomove(0, (25/3) * 2)
                        gegensteuerung()
                        print("Sturz")
                    for q in range(len(falllist)):
                            if distanz(mario[248], falllist[q]) < 10:
                                print("Stopp")
                                safe = 0
                window.update()
                x, y = hole_koord(mario[247])
                if y > 800:
                    leben -= 100

    def levelminus():
        global todcounter
        global leben
        if todcounter < 1:
            leben += -1
            todcounter = 5
    def tod():
        global leben
        global todcounter
        global level
        todcounter += -1
        if leben < 1:
            #pygame.mixer.music.pause()
            #pygame.mixer.Sound.play(deathsound)
            print("Tod")
            c.create_text(850, 300, text="GAME OVER!", font=("Lato Heavy", 60), fill = 'white')
            c.create_text(850, 370, text="Du bist soeben gestorben!", font=("Helvetica", 30), fill = 'white')
            c.create_text(850, 410, text = "Punkte: " + str(points), font = ("Helvetica", 30), fill = 'white')
            text = open("level.txt", "w")
            text.write(str(level))
            text.close()
    def levelup():
        global level
        global bewegungserlaubnis
        for i in range(len(flag)):
           if distanz(mario[143], flag[i]) < 50:
                for q in range(0, 12):
                    c.move(flag[i], 0, 25/3 * 2)
                    sprung()
                    sturz
                    gegensteuerung()
                    window.update()
                    sleep(0.01)
                for q in range(0, 40):
                    c.move(goodflag, 0, -5)
                    window.update()
                    sleep(0.01)
                level += 1
               #pygame.mixer.music.pause()
              # pygame.mixer.Sound.play(levelsound)
    bewegungscounter = 0
    marionorm(1)
    def ebene1():
        ebeninit(1)
        eben1(ebene11, 1)
        ebene(ebene12, 600,0)
        ebene(ebene13, 550,0)
        ebene(ebene14, 500,0)
        ebene(ebene15, 450,0)
        ebene(ebene16, 400,0)
        ebene(ebene17, 350,0)
        window.update()
    ebene1()
    c.create_text(75, 30, text='Punkte', fill = 'black', font = ('Bitstream Vera Sans', 30))
    c.create_text(600,30,fill="red2", text="Welt 1 - Level ", font=("Bitstream Vera Sans", 30))
    punkttext = c.create_text(250, 30, fill = 'black', font = ('eufm10', 30))
    leveltext = c.create_text(775,30, fill="red2", font=("eufm10",30))
    c.create_text(900, 30, fill='red2', text='Leben', font=("eufmio10", 30))
    lebentext = c.create_text(990, 30, fill ='red2', font=("eufmio10", 30))
    def plattform1():
        for i in range(len(plattform)):
            if distanz(mario[245],plattform[i])<15:
                for i in range(len(plattform)):
                    c.move(plattform[i], 1,0)
                mariomove(1,0)
                global bewegungscounter
                bewegungscounter+=1
    while leben >0 and level == 1:
        bowserfunc()
        feuermod()
        sprung()
        sturz()
        punkte()
        bewegung()
        enemy()
       # feuermarionormal()
        tod()
        levelup()
        c.itemconfig(punkttext, text = str(points))
        c.itemconfig(leveltext,text=str(level))
        c.itemconfig(lebentext, text=str(leben))
        gegensteuerung()
        window.update()
        under(1,ebene1under, eben1norm)
        #pygame.mixer.music.unpause()
    if leben > 0:
        sleep(1)
        restart()
        rechts2 = False
        links2 = False
        ebeninit(1)
        eben1(ebene21,1)
        ebene(ebene22, 600,0)
        ebene(ebene23, 550,0)
        ebene(ebene24, 500,0)
        ebene(ebene25, 450,0)
        ebene(ebene26, 400,0)
        ebene(ebene27, 350,0)
        window.update()
        print(level)
        undergroundlevel = 1
    while level == 2 and leben>0:
        feuermod()
        kaufen()
        sprung()
        sturz()
        punkte()
       # feuermarionormal()
        bewegung()
        enemy()
        tod()
        levelup()
        c.itemconfig(punkttext, text = str(points))
        c.itemconfig(leveltext,text=str(level))
        c.itemconfig(lebentext, text=str(leben))
        gegensteuerung()
        window.update()
        sleep(0.05)
       # pygame.mixer.music.unpause()
    if leben > 0:
        sleep(1)
        restart()
        rechts2 = False
        links2 = False
        ebeninit(1)
        eben1(ebene31,1)
        ebene(ebene32, 600,0)
        ebene(ebene33, 550,0)
        ebene(ebene34, 500,0)
        ebene(ebene35, 450,0)
        ebene(ebene36, 400,0)
        ebene(ebene37, 350,0)
        window.update()
        print(level)
    while level == 3 and leben>0:
        under(1, eben3under, eben3norm)
        feuermod()
        sprung()
        sturz()
        punkte()
        kaufen()
        bewegung()
        enemy()
       # feuermarionormal()
        tod()
        levelup()
        c.itemconfig(punkttext, text = str(points))
        c.itemconfig(leveltext,text=str(level))
        c.itemconfig(lebentext, text=str(leben))
        gegensteuerung()
        window.update()
       # pygame.mixer.music.unpause()
    if leben > 0:
        sleep(1)
        restart()
        rechts2 = False
        links2 = False
        ebeninit(1)
        eben1(ebene41,0)
        ebene(ebene42, 600,0)
        window.update()
        print(level)
        undergroundlevel = 1
        lastposition = 0

    while level == 4 and leben>0:
        #under(1, ebene3under, eben3norm)
        feuermod()
        sprung()
        sturz()
        kaufen()
        punkte()
        bewegung()
        enemy()
        bowserfunc()
       # feuermarionormal()
        tod()
        levelup()
        c.itemconfig(punkttext, text = str(points))
        c.itemconfig(leveltext,text=str(level))
        c.itemconfig(lebentext, text=str(leben))
        gegensteuerung()
        window.update()
       # pygame.mixer.music.unpause()
    if leben > 0:
        sieg = c.create_text(850, 300, text="Sieg!", font=("Lato Heavy", 60))
        punkte10 = c.create_text(850, 410, text = "Punkte: " + str(points), font = ("Helvetica", 30))
        restart()
        ebeninit(1)
        eben1(ebene43,0)
        ebene(ebene46, 600,0)
        ebene(ebene47, 550,0)
        ebene(ebene48, 500,0)
        ebene(ebene49, 450, 0)
        ebene(ebene50, 400 ,0)
        ebene(ebene51, 350,0)
        ebene(ebene52, 300,0)
        ebene(ebene53, 250,0)
        window.update()
        levelup()
        sleep(1)
        c.delete(sieg)
        c.delete(punkte10)
    while level == 5 and leben > 0:
        sprung()
        sturz()
        punkte()
        bewegung()
        enemy()
        tod()
        c.itemconfig(punkttext, text = str(points))
        c.itemconfig(leveltext,text=str(level))
        c.itemconfig(lebentext, text=str(leben))
        gegensteuerung()
        if bewegungscounter < 250:
            plattform1()
        window.update()
    sleep(3)
    restart()
    window.destroy()
