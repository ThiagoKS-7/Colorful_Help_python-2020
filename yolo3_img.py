

"""
Course:  Training YOLO v3 for Objects Detection with Custom Data
Edits: Thiago Kasper de Souza

Section-2
Objects Detection on Image with YOLO v3 and OpenCV
File: yolo-3-image.py
"""


# Detecting Objects on Image with OpenCV deep learning library
#
# Algorithm:
# Reading RGB image --> Getting Blob --> Loading YOLO v3 Network -->
# --> Implementing Forward Pass --> Getting Bounding Boxes -->
# --> Non-maximum Suppression --> Drawing Bounding Boxes with Labels
#
# Result:
# Window with Detected Objects, Bounding Boxes and Labels

def IA_2():
    # Importing needed libraries
    import numpy as np
    import cv2
    #import time
    import imageio
    from matplotlib import pyplot as plt
    import pyttsx3

    pred = []  
    engine=pyttsx3.init()
    engine.setProperty('voice','pt')
    
    
    """
    Start of:
    Reading input image
    """
    
    # Reading image with OpenCV library
    # In this way image is opened already as numpy array
    # WARNING! OpenCV by default reads images in BGR format
    # Pay attention! If you're using Windows, the path might looks like:
    # r'images\woman-working-in-the-office.jpg'
    # or:
    # 'images\\woman-working-in-the-office.jpg'
    
    captura = cv2.VideoCapture(0)
    cont = 0
        
    while True:
        ret, frame = captura.read()
        cont += 1
        if cont >= 25:
            break
            
    
    cv2.imwrite('new_img.jpg', frame)
    captura.release()
    cv2.destroyAllWindows()
        
    #img = "C:/Users/W10/OneDrive - liberato.com.br/Imagens/teste.jpg"
    image_BGR = cv2.imread('new_img.jpg')
    # Showing Original Image
    # Giving name to the window with Original Image
    # And specifying that window is resizable
    #cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    # Pay attention! 'cv2.imshow' takes images in BGR format
    #cv2.imshow('Original Image', image_BGR)
    # Waiting for any key being pressed
    #cv2.waitKey(0)
    # Destroying opened window with name 'Original Image'
    #cv2.destroyWindow('Original Image')
    
    # # Check point
    # # Showing image shape
    #print('Image shape:', image_BGR.shape)  # tuple of (511, 767, 3)
    
    # Getting spatial dimension of input image
    h, w = image_BGR.shape[:2]  # Slicing from tuple only first two elements
    
    # # Check point
    # # Showing height an width of image
    # print('Image height={0} and width={1}'.format(h, w))  # 511 767
    
    """
    End of: 
    Reading input image
    """
    
    
    """
    Start of:
    Getting blob from input image
    """
    
    # Getting blob from input image
    # The 'cv2.dnn.blobFromImage' function returns 4-dimensional blob
    # from input image after mean subtraction, normalizing, and RB channels swapping
    # Resulted shape has number of images, number of channels, width and height
    # E.G.:
    # blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size, mean, swapRB=True)
    blob = cv2.dnn.blobFromImage(image_BGR, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    
    # # Check point
    #print('Image shape:', image_BGR.shape)  # (511, 767, 3)
    #print('Blob shape:', blob.shape)  # (1, 3, 416, 416)
    
    # # Check point
    # # Showing blob image in OpenCV window
    # # Slicing blob image and transposing to make channels come at the end
    #blob_to_show = blob[0, :, :, :].transpose(1, 2, 0)
    #print(blob_to_show.shape)  # (416, 416, 3)
    #
    # # Showing Blob Image
    # # Giving name to the window with Blob Image
    # # And specifying that window is resizable
    #cv2.namedWindow('Blob Image', cv2.WINDOW_NORMAL)
    # # Pay attention! 'cv2.imshow' takes images in BGR format
    # # Consequently, we DO need to convert image from RGB to BGR firstly
    # # Because we have our blob in RGB format
    #cv2.imshow('Blob Image', cv2.cvtColor(blob_to_show, cv2.COLOR_RGB2BGR))
    # # Waiting for any key being pressed
    #cv2.waitKey(0)
    # # Destroying opened window with name 'Blob Image'
    #cv2.destroyWindow('Blob Image')
    
    """
    End of:
    Getting blob from input image
    """
    
    
    """
    Start of:
    Loading YOLO v3 network
    """
    
    # Loading COCO class labels from file
    # Opening file
    # Pay attention! If you're using Windows, yours path might looks like:
    # r'yolo-coco-data\coco.names'
    # or:
    # 'yolo-coco-data\\coco.names'
    with open('yolo-coco-data/coco.names') as f:
        # Getting labels reading every line
        # and putting them into the list
        labels = [line.strip() for line in f]
    
    
    # # Check point
    # print('List with labels names:')
    # print(labels)
    
    # Loading trained YOLO v3 Objects Detector
    # with the help of 'dnn' library from OpenCV
    # Pay attention! If you're using Windows, yours paths might look like:
    # r'yolo-coco-data\yolov3.cfg'
    # r'yolo-coco-data\yolov3.weights'
    # or:
    # 'yolo-coco-data\\yolov3.cfg'
    # 'yolo-coco-data\\yolov3.weights'
    network = cv2.dnn.readNetFromDarknet('yolo-coco-data/yolov3.cfg',
                                         'yolo-coco-data/yolov3.weights')
    
    # Getting list with names of all layers from YOLO v3 network
    layers_names_all = network.getLayerNames()
    
    # # Check point
    # print()
    # print(layers_names_all)
    
    # Getting only output layers' names that we need from YOLO v3 algorithm
    # with function that returns indexes of layers with unconnected outputs
    layers_names_output = \
        [layers_names_all[i[0] - 1] for i in network.getUnconnectedOutLayers()]
    # # Check point
    # print()
    # print(layers_names_output)  # ['yolo_82', 'yolo_94', 'yolo_106']
    
    # Setting minimum probability to eliminate weak predictions
    probability_minimum = 0.5
    
    # Setting threshold for filtering weak bounding boxes
    # with non-maximum suppression
    threshold = 0.3
    
    # Generating colours for representing every detected object
    # with function randint(low, high=None, size=None, dtype='l')
    colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')
    
    # # Check point
    # print()
    # print(type(colours))  # <class 'numpy.ndarray'>
    # print(colours.shape)  # (80, 3)
    # print(colours[0])  # [172  10 127]
    
    """
    End of:
    Loading YOLO v3 network
    """
    
    
    """
    Start of:
    Implementing Forward pass
    """
    
    # Implementing forward pass with our blob and only through output layers
    # Calculating at the same time, needed time for forward pass
    network.setInput(blob)  # setting blob as input to the network
    #start = time.time()
    output_from_network = network.forward(layers_names_output)
    #end = time.time()
    
    # Showing spent time for forward pass
    #print('Objects Detection took {:.5f} seconds'.format(end - start))
    
    """
    End of:
    Implementing Forward pass
    """
    
    
    """
    Start of:
    Getting bounding boxes
    """
    
    # Preparing lists for detected bounding boxes,
    # obtained confidences and class's number
    bounding_boxes = []
    confidences = []
    class_numbers = []
    
    
    # Going through all output layers after feed forward pass
    for result in output_from_network:
        # Going through all detections from current output layer
        for detected_objects in result:
            # Getting 80 classes' probabilities for current detected object
            scores = detected_objects[5:]
            # Getting index of the class with the maximum value of probability
            class_current = np.argmax(scores)
            # Getting value of probability for defined class
            confidence_current = scores[class_current]
    
            # # Check point
            # # Every 'detected_objects' numpy array has first 4 numbers with
            # # bounding box coordinates and rest 80 with probabilities for every class
            # print(detected_objects.shape)  # (85,)
    
            # Eliminating weak predictions with minimum probability
            if confidence_current > probability_minimum:
                # Scaling bounding box coordinates to the initial image size
                # YOLO data format keeps coordinates for center of bounding box
                # and its current width and height
                # That is why we can just multiply them elementwise
                # to the width and height
                # of the original image and in this way get coordinates for center
                # of bounding box, its width and height for original image
                box_current = detected_objects[0:4] * np.array([w, h, w, h])
    
                # Now, from YOLO data format, we can get top left corner coordinates
                # that are x_min and y_min
                x_center, y_center, box_width, box_height = box_current
                x_min = int(x_center - (box_width / 2))
                y_min = int(y_center - (box_height / 2))
    
                # Adding results into prepared lists
                bounding_boxes.append([x_min, y_min, int(box_width), int(box_height)])
                confidences.append(float(confidence_current))
                class_numbers.append(class_current)
    
    """
    End of:
    Getting bounding boxes
    """

    """
    Start of:
    Non-maximum suppression
    """
    
    # Implementing non-maximum suppression of given bounding boxes
    # With this technique we exclude some of bounding boxes if their
    # corresponding confidences are low or there is another
    # bounding box for this region with higher confidence
    
    # It is needed to make sure that data type of the boxes is 'int'
    # and data type of the confidences is 'float'
    # https://github.com/opencv/opencv/issues/12789
    results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                               probability_minimum, threshold)
    
    """
    End of:
    Non-maximum suppression
    """
    
    
    """
    Start of:
    Drawing bounding boxes and labels
    """
    
    # Defining counter for detected objects
    counter = 1
    
    # Checking if there is at least one detected object after non-maximum suppression
    if len(results) > 0:
        # Going through indexes of results
        for i in results.flatten():
            # Showing labels of the detected objects
            print('Objeto {0}: {1}'.format(counter, labels[int(class_numbers[i])]))
            pred.append(labels[int(class_numbers[i])])
            # Incrementing counter
            counter += 1
    
            # Getting current bounding box coordinates,
            # its width and height
            x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
            box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]
    
            # Preparing colour for current bounding box
            # and converting from numpy array to list
            colour_box_current = colours[class_numbers[i]].tolist()
    
            # # # Check point
            # print(type(colour_box_current))  # <class 'list'>
            # print(colour_box_current)  # [172 , 10, 127]
    
            # Drawing bounding box on the original image
            cv2.rectangle(image_BGR, (x_min, y_min),
                          (x_min + box_width, y_min + box_height),
                          colour_box_current, 2)
    
            # Preparing text with label and confidence for current bounding box
            text_box_current = '{}: {:.4f}'.format(labels[int(class_numbers[i])],
                                                   confidences[i])
    
            # Putting text with label and confidence on the original image
            cv2.putText(image_BGR, text_box_current, (x_min, y_min - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 0.7, colour_box_current, 2)
     
    cv2.imwrite("new_img.jpg",image_BGR)
    #salvar imagem pra corrigir cores
    image_RGB = imageio.imread("new_img.jpg")
    

    #mostrar imagem no pyplot
    plt.imshow(image_RGB)
    plt.show()
    
    # Comparing how many objects where before non-maximum suppression
    # and left after
    print()
    print('Total de objetos detectados:', len(bounding_boxes))
    print('Objetos deixados após non-maximum suppression:', counter - 1)
    if (counter - 1) >= 2:
        engine.say("Eu encontrei" + str(counter - 1) + "objetos.")
        engine.runAndWait()
    else:
        pass
    """
    End of:
    Drawing bounding boxes and labels
    """
    #print("predições: " + pred)
    
    if (counter - 1) == 1:
            num = 0
            #ext = texto[14:16]
            #print(ext)
            
            a = [0,1,3,9,11,18,19,22,23,24,26,27,28,39,40,43,44,45,46,47,49,51,
                 53,56,57,59,60,61,70,71,76,79]
            
            b = [2,4,5,6,7,8,10,12,13,14,15,16,17,20,21,25,29,
                 30,31,32,33,34,35,36,37,38,41,42,48,50,52,54,55,58,
                 62,63,64,65,66,67,68,69,72,73,74,75,77,78,80]
                
            j = 0
            while j < len(b):
                if (j < 32 and pred[num] == labels[a[j]]):        
                    engine.say("isso é uma" + pred[num] )
                    engine.runAndWait()
                    j += 1
                elif (j < 48 and pred[num - 1] == labels[b[j]]):
                    engine.say("isso é um" + pred[num])
                    engine.runAndWait()                
                else: 
                    j+= 1  
    else:
        
        import speech_recognition as sr
        r = sr.Recognizer()
    
        mic = sr.Microphone()
    
        with mic as fonte:
            r.adjust_for_ambient_noise(fonte)
            #print("Saudações, estou aguardando o seu comando")
            engine.say("O que devo fazer em seguida?")
            engine.runAndWait()
            audio= r.listen(fonte)
            print("um momento...")
            try:
                texto= r.recognize_google(audio, language="pt-BR")
                print("Você disse: {}".format(texto)) 
            except:
                print("não entendi .-.")
             
            #FRASES QUE ELA ENTENDE:
        if len(texto) == 16:       
                
            if texto == "defina objeto um" :
                num = 1
                #ext = texto[14:16]
                #print(ext)
                
                a = [0,1,3,9,11,18,19,22,23,24,26,27,28,39,40,43,44,45,46,47,49,51,
                     53,56,57,59,60,61,70,71,76,79]
                
                b = [2,4,5,6,7,8,10,12,13,14,15,16,17,20,21,25,29,
                     30,31,32,33,34,35,36,37,38,41,42,48,50,52,54,55,58,
                     62,63,64,65,66,67,68,69,72,73,74,75,77,78,80]
                    
                j = 0
                while j < len(b):
                    if (j < 32 and pred[num - 1] == labels[a[j]]):        
                        engine.say("isso é uma" + pred[num-1] )
                        engine.runAndWait()
                        j += 1
                    elif (j < 48 and pred[num - 1] == labels[b[j]]):
                        engine.say("isso é um" + pred[num - 1])
                        engine.runAndWait()                
                    else: 
                        j+= 1   
                        
        elif len(texto) == 15:
            corte = texto[14]
            num = int(corte)
            print (num) 
            print (pred[num - 1])
            #teste = "defina objeto"
            #print (len(teste + corte))
            if texto == "defina objeto " + corte:
                
                c= [0,1,3,9,11,18,19,22,23,24,26,27,28,39,40,43,44,45,46,47,49,51,
                     53,56,57,59,60,61,70,71,76,79]
                
                d = [2,4,5,6,7,8,10,12,13,14,15,16,17,20,21,25,29,
                     30,31,32,33,34,35,36,37,38,41,42,48,50,52,54,55,58,
                     62,63,64,65,66,67,68,69,72,73,74,75,77,78,80]
                
                k = 0
                while k < len(d):
                    if (k < 32 and pred[num - 1] == labels[c[k]]):        
                        engine.say("isso é uma" + pred[num - 1] )
                        engine.runAndWait()
                        k += 1
                    elif (k < 48 and pred[num - 1] == labels[d[k]]):
                        engine.say("isso é um" + pred[num - 1])
                        engine.runAndWait()
                        k += 1                      
                    else: 
                        k += 1
                 
                
        engine.stop()     
    
"""
Some comments
    
With OpenCV function 'cv2.dnn.blobFromImage' we get 4-dimensional
so called 'blob' from input image after mean subtraction,
normalizing, and RB channels swapping. Resulted shape has:
- number of images
- number of channels
- width
- height
E.G.: blob = cv2.dnn.blobFromImage(image, scalefactor=1.0, size, mean, swapRB=True)
"""

IA_2()