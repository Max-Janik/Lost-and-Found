#IMPORTS
import pygame
import os
import socket

class APP:

    #DEF's


    def __init__(self):

        
        pygame.init()
        android = True
        #DEFINE SCREEN SIZE FOR DESKTOP TESTING
        screen = pygame.display.set_mode((720/2, 1280/2))
        #GET SCREEN HEIGHT AND WIDTH
        screen_w, screen_h = screen.get_size()
        #DEFINE RELATIVE SIZES
        button_h = screen_h*0.1
        button_w = screen_w/3
        header_h = 1.5 * button_h
        #LOADING "NEARBY" BUTTON ICON
        BNB_Icon = pygame.image.load("BNB-icon.png")
        BNB_Icon = pygame.transform.scale(BNB_Icon, (int(button_w),int(button_h)))
        HNB_Icon = pygame.image.load("HNB-icon.png")
        HNB_Icon = pygame.transform.scale(HNB_Icon, (int(button_w),int(button_h)))
        
        #LOADING "NEW ITEM" BUTTON ICON
        BN_Icon = pygame.image.load("BN-icon.png")
        BN_Icon = pygame.transform.scale(BN_Icon, (int(button_w),int(button_h)))
        HN_Icon = pygame.image.load("HN-icon.png")
        HN_Icon = pygame.transform.scale(HN_Icon, (int(button_w),int(button_h)))

        #LOADING "FOUND" BUTTON ICON
        BF_Icon = pygame.image.load("BF-icon.png")
        BF_Icon = pygame.transform.scale(BF_Icon, (int(button_w),int(button_h)))
        HF_Icon = pygame.image.load("HF-icon.png")
        HF_Icon = pygame.transform.scale(HF_Icon, (int(button_w),int(button_h)))

        #LOADING HEADER
        Header_Icon = pygame.image.load("Header-icon.png")
        Header_Icon = pygame.transform.scale(Header_Icon, (int(screen_w),int(header_h)))

        #LOADING FONTS
        try:
            pygame.font.init()
            font = pygame.font.Font('DejaVuSans.ttf', 20)
            print "Font loaded correctly!"
        except Exception as fe:
            print "Font Error!"
            print fe

        
            
        #SETTING UP THE SCREEN LAYOUT
        screen.fill((255, 255, 255))    
        button1 = screen.blit(BNB_Icon, [0, button_h*9])
        button2 = screen.blit(BN_Icon, [button_w, button_h*9])
        button3 = screen.blit(BF_Icon, [2*button_w, button_h*9])
        Header = screen.blit(Header_Icon, [0,0])
        pygame.display.flip()

        #ERASE SCREEN CONTENT BETWEEN HEADER AND BUTTONS
        def erase():
            screen.fill((255, 255, 255), (0,int(header_h),screen_w,int(0.75*screen_h)))
            pygame.display.flip()

        

        #ACTUAL PROGRAMM
        while True:

            
            #WAIT FOR EVENT TO OCCUR
            event = pygame.event.wait()

            
            
            # PYGAME QUIT
            if event.type == pygame.QUIT:
                break



            #HITTING THE SCREEN
            elif event.type == pygame.MOUSEBUTTONDOWN:

                #BUTTON 1 | ESTABLISHING CONNECTION
                if button1.collidepoint(event.pos):

                    #BUTTON PRESS ANIMATION
                    button1 = screen.blit(HNB_Icon, [0, button_h*9])
                    pygame.display.flip()
                    try:
                        #eSTABLISHING SOCKET SERVER
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        
                        erase()
                        #FOR DEBUGGING ONLY
                        textsurface = font.render("Socket Works!", False, (0, 0, 0))
                        screen.blit(textsurface,(0,header_h))
                        pygame.display.flip()

                        #FOR LOCAL AND GLOBAL TESTING
                        global_ip = "Lost-and-Found-app.de"
                        local_ip = "192.168.2.105"
                        #CONNECTING TO SOCKET SERVER
                        s.connect((global_ip,3389))
                        print s.recv(1024)
                        print s.recv(1024)
                        print s.recv(1024)
                        #FOR DEBUGGING ONLY
                        textsurface = font.render("Connected!", False, (0, 0, 0))
                        screen.blit(textsurface,(0,1.25*header_h))
                        pygame.display.flip()
                        
                        #RECIVE FILE FROM SERVER
                        with open('empfangen.jpg','wb') as f:
                            while True:
                                recv = s.recv(1024)
                                f.write(recv)
                                s.send("1")
                                textsurface = font.render("1 Datei von Server her", False, (0, 0, 0))
                                screen.blit(textsurface,(0,1.75*header_h))
                                pygame.display.flip()
                                if len(recv) < 1024:
                                    break

                        #FOR DEBUGGING ONLY
                        textsurface = font.render("Recieved Data!", False, (0, 0, 0))
                        screen.blit(textsurface,(0,1.5*header_h))
                        pygame.display.flip()

                        #CLOSE CONNECTIONS
                        f.close()
                        s.send("1")
                        s.close()
                        
                        erase()
                        #SHOW RECIEVED IMAGE ON SCREEN
                        prnt = pygame.image.load("empfangen.jpg")
                        prnt = pygame.transform.scale(prnt,(screen_w,button_h*7.5))
                        screen.blit(prnt,(0,header_h))
                        pygame.display.flip()
                        
                    except Exception as ex:
                        print "Connection Error"
                        print str(ex)
                        #erase()
                        ex = str(ex)
                        textsurface = font.render(ex, False, (0, 0, 0))
                        screen.blit(textsurface,(0,2*header_h))
                        pygame.display.flip()
                        
                #BUTTON 2 | NO FUNCTION; CHANGING SELF.COLOR      
                elif button2.collidepoint(event.pos):
                    
                    button2 = screen.blit(HN_Icon, [button_w, button_h*9])
                    pygame.display.flip()

                #BUTTON 3 | NO FUNCTION; CHANGING SELF.COLOR  
                elif button3.collidepoint(event.pos):
                    
                    button3 = screen.blit(HF_Icon, [2*button_w, button_h*9])
                    pygame.display.flip()


            try:

                if android:
                    # ANDROID BACK KEY
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_AC_BACK:
                        break


                    #LETTING GO OF BUTTONS
                    elif event.type == pygame.MOUSEBUTTONUP:
                        
                        button1 = screen.blit(BNB_Icon, [0, button_h*9])
                        button2 = screen.blit(BN_Icon, [button_w, button_h*9])
                        button3 = screen.blit(BF_Icon, [2*button_w, button_h*9])
                        pygame.display.flip()



                    
                    elif event.type == pygame.APP_WILLENTERBACKGROUND:

                        print "sleeping now"
                    elif event.type == pygame.APP_DIDENTERFOREGROUND:
                        
                        #SETTING UP THE SCREEN AFTER REENTERING THE APP
                        screen = pygame.display.set_mode((1280, 720))
                        screen.fill((255, 255, 255))    
                        button1 = screen.blit(BNB_Icon, [0, button_h*9])
                        button2 = screen.blit(BN_Icon, [button_w, button_h*9])
                        button3 = screen.blit(BF_Icon, [2*button_w, button_h*9])
                        Header = screen.blit(Header_Icon, [0,0])
                        pygame.display.flip()
            except:
                android == False #PREVENTING CRASH ON DESKTOP

        #QUITS THE APP WHEN BREAKING OUT THE WHILE LOOP
        pygame.quit()




#MAIN
    
if __name__ == "__main__":
    APP()
#END


#NOTES:

#python android.py build app release install --launch
#font: Tw Cen MT Condensed, Bold
