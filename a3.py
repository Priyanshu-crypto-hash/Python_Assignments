import numpy as np
import matplotlib.pyplot as plt
# NO other imports are allowed

class Shape:
    '''
    DO NOT MODIFY THIS CLASS

    DO NOT ADD ANY NEW METHODS TO THIS CLASS
    '''
    def __init__(self):
        self.T_s = None
        self.T_r = None
        self.T_t = None
    
    
    def translate(self, dx, dy):
        '''
        Polygon and Circle class should use this function to calculate the translation
        '''
        self.T_t = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
 

    def scale(self, sx, sy):
        '''
        Polygon and Circle class should use this function to calculate the scaling
        '''
        self.T_s = np.array([[sx, 0, 0], [0, sy, 0], [0, 0, 1]])
 
        
    def rotate(self, deg):
        '''
        Polygon and Circle class should use this function to calculate the rotation
        '''
        rad = deg*(np.pi/180)
        self.T_r = np.array([[np.cos(rad), np.sin(rad), 0],[-np.sin(rad), np.cos(rad),0], [0, 0, 1]])

        
    def plot(self, x_dim, y_dim):
        '''
        Polygon and Circle class should use this function while plotting
        x_dim and y_dim should be such that both the figures are visible inside the plot
        '''
        x_dim, y_dim = 1.2*x_dim, 1.2*y_dim
        plt.plot((-x_dim, x_dim),[0,0],'k-')
        plt.plot([0,0],(-y_dim, y_dim),'k-')
        plt.xlim(-x_dim,x_dim)
        plt.ylim(-y_dim,y_dim)
        plt.grid()
        plt.show()



class Polygon(Shape):
    '''
    Object of class Polygon should be created when shape type is 'polygon'
    '''
    def __init__(self, A):
        '''
        Initializations here
        '''
        self.A=A
        self.x_new = None
        self.y_new = None
        self.x_cord=[]
        self.y_cord=[]
        self.old_matrix=self.A.copy()


    def translate(self, dx, dy):
        '''
        Function to translate the polygon
    
        This function takes 2 arguments: dx and dy
    
        This function returns the final coordinates
        '''
        Shape.translate(self,dx,dy)
        temp_matrix=np.array(self.T_t).transpose() #create a temporary matrix to perfor the translate operation
        new_matrix=np.around(np.dot(self.A,temp_matrix),2) #round of the final matrix till 2 decimal places
        self.x_new=(np.array(new_matrix).transpose()[0])
        self.y_new=(np.array(new_matrix).transpose()[1])
        self.old_matrix=self.A.copy()# to print the previous output
        self.A=new_matrix  # to update the matrix after performing translating
        return self.x_new,self.y_new



    def scale(self, sx, sy):
        '''
        Function to scale the polygon
    
        This function takes 2 arguments: sx and sx
    
        This function returns the final coordinates
        '''
        Shape.scale(self,sx,sy)
        row_1=[]
        row_2=[]
        row_3=[]
        length_x=(len(np.array(self.A).transpose()[0]))
        x_centre=(sum(np.array(self.A).transpose()[0]))/length_x#to find the centre of the polygon
        y_centre=(sum(np.array(self.A).transpose()[1]))/length_x
        for i in range(length_x):
            row_1.append(x_centre)
        for j in range(length_x):
            row_2.append(y_centre)
        for k in range(length_x):
            row_3.append(0)
        new_matrix=np.array([row_1,row_2,row_3])#to create a matrix that has rows as centre x coordinates ,centre y coordinates and 0 as its entry
        t_new_matrix=np.array(new_matrix).transpose()
        subtracted_matrix=(self.A-t_new_matrix)
        scaled_matrix=np.dot(subtracted_matrix,self.T_s)
        added_matrix=scaled_matrix+t_new_matrix
        final_matrix=np.around(added_matrix,2)#round of the final matrix till 2 decimal places
        t_final_matrix=np.array(final_matrix).transpose()
        self.x_new=t_final_matrix[0]
        self.y_new=t_final_matrix[1]
        self.old_matrix = self.A.copy()# to create print the previous output
        self.A = final_matrix# to update the matrix after performing translating
        return self.x_new,self.y_new

    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the polygon

        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates
        '''
        Shape.rotate(self,deg)
        row_1 = []
        row_2 = []
        row_3 = []
        for i in range(len(np.array(self.A).transpose()[0])):
            temp_row_1=row_1.append(rx)
        for j in range(len(np.array(self.A).transpose()[1])):
            temp_row_2=row_2.append(ry)
        for k in range(len(np.array(self.A).transpose()[0])):
            temp_row_3=row_3.append(0)
        new_matrix=np.array([row_1,row_2,row_3])#to create a matrix that has rows as x coordinates ,y coordinates and 0 as its entry
        t_new_matrix=np.array(new_matrix.transpose())
        sub_matrix=(self.A-t_new_matrix)
        new_matrix2=np.dot(sub_matrix,np.array(self.T_r).transpose())
        final_matrix=np.around((new_matrix2+t_new_matrix),2)#round of the final matrix till 2 decimal places
        t_final_matrix=np.array(final_matrix).transpose()
        self.x_new=t_final_matrix[0]
        self.y_new=t_final_matrix[1]
        self.old_matrix = self.A.copy()
        self.A = final_matrix# to update the matrix after performing translating
        return self.x_new,self.y_new

    def plot(self):
        '''
        Function to plot the polygon
    
        This function should plot both the initial and the transformed polygon
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        for i in self.A:
            self.x_cord.append(i[0])
        for j in self.A:
            self.y_cord.append(j[1])
        self.x_cord.append(self.x_cord[0]) #to make polygon last element of the list should be same as first element
        self.y_cord.append(self.y_cord[0])
        plt.plot(self.x_cord, self.y_cord, color='black')
        self.x_cord = []
        self.y_cord = []
        for k in self.old_matrix:
            self.x_cord.append(k[0])
        for l in self.old_matrix:
            self.y_cord.append(l[1])
        self.x_cord.append(self.x_cord[0])
        self.y_cord.append(self.y_cord[1])
        plt.plot(self.x_cord, self.y_cord, color='black', linestyle='dashed')
        Shape.plot(self,max(max(self.A[0]),max(self.old_matrix[0]) ,abs(min(self.A[0])),abs(min(self.old_matrix[0]))),max(max(self.A[1]),max(self.old_matrix[1]) ,abs(min(self.A[1])),abs(min(self.old_matrix[1]))))#to increase the scale of the graph
        self.x_cord = []
        self.y_cord = []



class Circle(Shape):
    '''
    Object of class Circle should be created when shape type is 'circle'
    '''
    def __init__(self, x=0, y=0, radius=5):
        '''
        Initializations here
        '''
        self.x=x
        self.y=y
        self.radius=radius
        self.A=[x,y,1]
        self.old_radius=radius
        self.old_matrix = self.A.copy()
    def translate(self, dx, dy):
        '''
        Function to translate the circle
    
        This function takes 2 arguments: dx and dy (dy is optional).
    
        This function returns the final coordinates and the radius
        '''
        Shape.translate(self,dx,dy)
        final_matrix=np.around(np.dot(self.A,np.array(self.T_t).transpose()),2) #makes a new matrix by multiplying the given cordinate matrix and the transpose of translating matrix to obtain the translated coordinates
        self.x_new=final_matrix[0]#assigns the row of matrix containig the new x cordinates to variable x_new
        self.y_new=final_matrix[1]#assigns the row of matrix containing the new y cordinates to variable y_new
        self.old_matrix=self.A.copy()
        self.A=final_matrix# to update the matrix after performing translating
        self.old_radius=self.radius
        return self.x_new,self.y_new,self.radius

    def scale(self, sx):
        '''
        Function to scale the circle
    
        This function takes 1 argument: sx
    
        This function returns the final coordinates and the radius
        '''
        Shape.scale(self,sx,sx)
        temp_matrix=np.array([self.radius,0,0])
        final_matrix=np.around(np.dot(temp_matrix,self.T_s),2)#round of the final matrix till 2 decimal places
        self.x_new=self.x
        self.y_new=self.y
        self.radius = final_matrix[0]#stores the first entry of the matrix as radius
        self.old_radius=self.radius
        return self.x_new,self.y_new,self.radius

    def rotate(self, deg, rx = 0, ry = 0):
        '''
        Function to rotate the circle
    
        This function takes 3 arguments: deg, rx(optional), ry(optional). Default rx and ry = 0. (Rotate about origin)
    
        This function returns the final coordinates and the radius
        '''
        Shape.rotate(self,deg)
        temp_matrix=np.array([rx,ry,0])
        sub_matrix=(self.A-temp_matrix)
        new_matrix=np.dot(sub_matrix,np.array(self.T_r).transpose())
        final_matrix=np.around((temp_matrix+new_matrix),2)#round of the final matrix till 2 decimal places
        self.x_new=final_matrix[0]
        self.y_new=final_matrix[1]
        self.x=self.x_new
        self.y=self.y_new
        self.A=final_matrix# to update the matrix after performing rotating
        self.old_matrix = self.A
        return self.x_new,self.y_new,self.radius


    def plot(self):
        '''
        Function to plot the circle
    
        This function should plot both the initial and the transformed circle
    
        This function should use the parent's class plot method as well
    
        This function does not take any input
    
        This function does not return anything
        '''
        figure, axes = plt.subplots()
        axes.set_aspect(1)
        x = self.old_matrix[0]
        y = self.old_matrix[1]
        axes.add_artist(plt.Circle((x, y), self.old_radius, fill=False, linestyle='--'))
        x = self.A[0]
        y = self.A[1]
        axes.add_artist(plt.Circle((x, y), self.radius, fill=False, ))
        Shape.plot(self, max(abs(self.A[0])+ self.radius,abs(self.old_matrix[0])+self.old_radius),max(abs(self.A[1])+ self.radius,abs(self.old_matrix[1])+self.old_radius))

if __name__ == "__main__":
    '''
    Add menu here as mentioned in the sample output section of the assignment document.
    '''
    verbose = int(input("verbose? 1 to plot, 0 otherwise: "))
    num_test_cases = int(input('Enter the number of test cases: '))

    for i in range(num_test_cases):
        figure_type = int(input('Enter type of shape (polygon(0)/circle(1)): '))
        if figure_type == 1:
            input_list = list(map(float, input("enter x,y,r space separated : ").split()))
            if len(input_list) != 0:
                circle = Circle(input_list[0], input_list[1], input_list[2])
            else:
                circle = Circle()
        if figure_type == 0:
            A = []
            num_sides = int(input('Enter the number of sides: '))
            for j in range(num_sides):
                coordinates = list(map(float, input(f'Enter x{j + 1}, y{j + 1} space separated : ').split()))
                coordinates.append(1)
                A.append(coordinates)
            polygon = Polygon(A)

        num_query = int(input('Enter the number of queries: '))
        print('''ENTER QUERY:
                 1) R deg (rx) (ry)
                 2) T dx (dy)
                 3) S sx (sy)
                 4) P''')
        if figure_type == 0:
            for l in range(num_query):
                circle_input = input().split()
                if circle_input[0].upper() == 'R':
                    if len(circle_input) == 2:
                        temp_var = polygon.rotate(float(circle_input[1]))
                        for k in polygon.old_matrix:
                            print(k[0], end=' ')
                        for k in polygon.old_matrix:
                            print(k[1], end=' ')
                        print("")
                        for t in temp_var[0]:
                            print(t, end=' ')
                        for t in temp_var[1]:
                            print(t, end=' ')
                        if verbose == 1:
                            polygon.plot()
                    elif len(circle_input) == 3:
                        temp_var = polygon.rotate(float(circle_input[1]), float(circle_input[2]))
                        for k in polygon.old_matrix:
                            print(k[0], end=' ')
                        for k in polygon.old_matrix:
                            print(k[1], end=' ')
                        print("")
                        for t in temp_var[0]:
                            print(t, end=' ')
                        for t in temp_var[1]:
                            print(t, end=' ')
                        if verbose == 1:
                            polygon.plot()
                    else:
                        temp_var = polygon.rotate(float(circle_input[1]), float(circle_input[2]),float(circle_input[3]))
                        for k in polygon.old_matrix:
                            print(k[0], end=' ')
                        for k in polygon.old_matrix:
                            print(k[1], end=' ')
                        print("")
                        for t in temp_var[0]:
                            print(t, end=' ')
                        for t in temp_var[1]:
                            print(t, end=' ')
                        if verbose == 1:
                            polygon.plot()
                elif circle_input[0].upper() == 'S':
                    if len(circle_input) == 2:
                        temp_var = polygon.scale(float(circle_input[1]), float(circle_input[1]))
                        for k in polygon.old_matrix:
                            print(k[0], end=' ')
                        for k in polygon.old_matrix:
                            print(k[1], end=' ')
                        print("")
                        for t in temp_var[0]:
                            print(t, end=' ')
                        for t in temp_var[1]:
                            print(t, end=' ')
                        if verbose == 1:
                            polygon.plot()
                    else:
                        temp_var = polygon.scale(float(circle_input[1]), float(circle_input[2]))
                        for k in polygon.old_matrix:
                            print(k[0], end=' ')
                        for k in polygon.old_matrix:
                            print(k[1], end=' ')
                        print("")
                        for t in temp_var[0]:
                            print(t, end=' ')
                        for t in temp_var[1]:
                            print(t, end=' ')
                        if verbose == 1:
                            polygon.plot()
                elif circle_input[0].upper() == 'T':
                    if len(circle_input) == 2:
                        temp_var = polygon.translate(float(circle_input[1]), float(circle_input[1]))
                        for k in polygon.old_matrix:
                            print(k[0], end=' ')
                        for k in polygon.old_matrix:
                            print(k[1], end=' ')
                        print("")
                        for t in temp_var[0]:
                            print(t, end=' ')
                        for t in temp_var[1]:
                            print(t, end=' ')
                        if verbose == 1:
                            polygon.plot()
                    else:
                        temp_var = polygon.translate(float(circle_input[1]), float(circle_input[2]))
                        for k in polygon.old_matrix:
                            print(k[0], end=' ')
                        for k in polygon.old_matrix:
                            print(k[1], end=' ')
                        print("")
                        for t in temp_var[0]:
                            print(t, end=' ')
                        for t in temp_var[1]:
                            print(t, end=' ')
                        if verbose == 1:
                            polygon.plot()
                elif circle_input[0].upper() == 'P':
                    polygon.plot()
        if figure_type == 1:
            for l in range(num_query):
                circle_input = input().split()
                if circle_input[0].upper() == 'R':
                    if len(circle_input) == 2:
                        temp_var = circle.rotate(float(circle_input[1]))
                        print([circle.x, circle.y, circle.radius])
                        for a in temp_var:
                            print(a, end=' ')
                        if verbose == 1:
                            circle.plot()
                    elif len(circle_input) == 3:
                        temp_var = circle.rotate(float(circle_input[1]), float(circle_input[2]))
                        print([circle.x, circle.y, circle.radius])
                        for a in temp_var:
                            print(a, end=' ')
                        if verbose == 1:
                            circle.plot()
                    else:
                        temp_var = circle.rotate(float(circle_input[1]), float(circle_input[2]), float(circle_input[3]))
                        print([circle.x, circle.y, circle.radius])
                        for a in temp_var:
                            print(a, end=' ')
                        if verbose == 1:
                            circle.plot()
                elif circle_input[0].upper() == 'S':
                    temp_var = circle.scale(float(circle_input[1]))
                    print([circle.x, circle.y, circle.radius])
                    for a in temp_var:
                        print(a, end=' ')
                    if verbose == 1:
                        circle.plot()
                elif circle_input[0].upper() == 'T':
                    if len(circle_input) == 2:
                        temp_var = circle.translate(float(circle_input[1]), float(circle_input[1]))
                        print([circle.x, circle.y, circle.radius])
                        for a in temp_var:
                            print(a, end=' ')
                        if verbose == 1:
                            circle.plot()
                    elif len(circle_input) == 3:
                        temp_var = circle.translate(float(circle_input[1]), float(circle_input[2]))
                        print([circle.x, circle.y, circle.radius])
                        for a in temp_var:
                            print(a, end=' ')
                        if verbose == 1:
                            circle.plot()
                elif circle_input[0].upper() == 'P':
                    circle.plot()














