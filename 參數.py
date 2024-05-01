import matplotlib.pyplot as plt

def create_plot(x, y):
    # Create a new figure
    fig = plt.figure(figsize=(6,6))

    # Add an axes to the figure
    ax = fig.add_subplot(111)
    ax = plt.subplot(projection= '3d')
    # Plot the data
    ax.plot(x, y)
    x = [2,4,6,8,10]*3
    y = [10]*5+[12]*5+[14]*5
    z = 1
    dz = [5,4,3,2,1,1,2,3,4,5,5,3,1,3,5]
    ax.bar3d(x,y,z,dx=1,dy=1,dz=dz)
    # Set labels for the x and y axes
    ax.set_xlabel('X values')
    ax.set_ylabel('Y values')

    # Set a title for the plot
    ax.set_title('Sample plot')

    # Display the plot
    plt.show()

# Generate some data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Call the function to create the plot
create_plot(x, y)
