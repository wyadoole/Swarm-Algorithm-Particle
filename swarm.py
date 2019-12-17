import random # imports ramdom libary to be used
import numpy as np# imports numpy to be used

print("The appication is swarm algorithm that has to do with paricle optimization. PSO is a compuerized method that opimizes a problem by iterativle tyring to imporve a cadidate solution with regards to a given measure of quality. "
      "In laymens terms the Application tryis to solve problems for the swarm of paricels to get the best position from the target to the paricle ")
W = 0.5# inertial parameter the affects the movement propagation given by the last velocity value
# acceleration coefficients

c1 = 0.8# value that give the personal best value
c2 = 0.9# value that give the social best value

n_iterations = input("Please enter the number of iterations: ")# takes in user input for the numebr of iterations
while n_iterations not in "123456789":# excemtpion handling so that the user cant input anything other then 123456790
    n_iterations = input("Please reenter the number of iterations: ")# has them input again
n_iterations = int(n_iterations)# takes the interation as ints
target_error = float(input("Please enter the target error: "))# ask for user inout for terget error
n_particles = input("Please enter the number of particles: ")# takes the user inout fro particles
while n_particles not in "123456789":# deos a while loop incase the user enter the wrong number
    n_particles = input("PLease reenter the number of particles: ")# ask tge question again
n_particles=int(n_particles)# take in user particles number



class Particle():# creates the particle to be used
    def __init__(self):
        self.position = np.array([(-1) ** (bool(random.getrandbits(1))) * random.random() * 50,
                                  (-1) ** (bool(random.getrandbits(1))) * random.random() * 50])# gets the position as list of an array
        self.pbest_position = self.position # gets the personal best paricel are posiiton
        self.pbest_value = float('inf')# gets the personal bets value
        self.velocity = np.array([0, 0])# then get sthe veolocity

    def __str__(self):# prints out the results
        print("I am at ", self.position, " Best indevidual position of Particle: ", self.pbest_position)# prints the position of the versonal best at that curent location

    def move(self):# sets the move
        self.position = self.position + self.velocity# gets the new position of the particle

# search spave controls the algorithm routine
class Space():

    def __init__(self, target, target_error, n_particles):# takes in peramtatrer
        self.target = target# gets the target
        self.target_error = target_error# gets teh target error
        self.n_particles = n_particles# gets the number of paricels
        self.particles = []# get the lsit of those paricels
        self.gbest_value = float('inf')# gets the globel best value as a flaot
        self.gbest_position = np.array([random.random() * 50, random.random() * 50]) # get the potion as an array as random

    def print_particles(self): # prints the paricles
        for particle in self.particles:# get the range of paricels to be used
            particle.__str__()# gets the list

    def fitness(self, particle):# get sthe fitness of each
        return particle.position[0] ** 2 + particle.position[1] ** 2 + 1 # returns the fitness of each

    def set_pbest(self):# sets personal best
        for particle in self.particles:# searches for personal best by fitness
            fitness_cadidate = self.fitness(particle)# gets fitniss cadidate
            if (particle.pbest_value > fitness_cadidate): # check to see if personal best is greater then fitness candiate
                particle.pbest_value = fitness_cadidate# if fitness = Personal best then take
                particle.pbest_position = particle.position # then checks position with that position

    def set_gbest(self):# sets the global best
        for particle in self.particles:# checks the globel best of all paricles in the entire applicaton
            best_fitness_cadidate = self.fitness(particle)# gets fitniss cadidate
            if (self.gbest_value > best_fitness_cadidate):# check to see if personal best is greater then fitness candiate
                self.gbest_value = best_fitness_cadidate# if fitness = Personal best then take
                self.gbest_position = particle.position# then checks position with that position

    def move_particles(self):# move the paricle while the applciation is running
        for particle in self.particles:# checks the paricle to be moved
            global W# getts the gobal inertial parameter the affects the movement propagation given by the last velocity value
            new_velocity = (W * particle.velocity) + (c1 * random.random()) * (
                        particle.pbest_position - particle.position) + \
                           (random.random() * c2) * (self.gbest_position - particle.position)# gets the new velocity
            particle.velocity = new_velocity # sets that new velocity to the paricle
            particle.move()# then moves that particel to a new position

#MAIN LOOP#
search_space = Space(1, target_error, n_particles)# sets the search space to space which takes in target error and number of paricles
particles_vector = [Particle() for _ in range(search_space.n_particles)]# gets the new paricle vector for the velocity
search_space.particles = particles_vector# searchs space for particel with new vector
search_space.print_particles()# print particle

iteration = 0 # sets the iteration to 0 at the begining of each run so that
while (iteration < n_iterations):# while the iteration is what the user sets at the beging of the run of the aplication
    search_space.set_pbest()# Sets the personal best from the space the being used by the location of that single particle
    search_space.set_gbest()# Sets the global best from the space fro all parcels  that are currently active

    if (abs(search_space.gbest_value - search_space.target) <= search_space.target_error):# seearchs for the target error
        break# returns nothing

    search_space.move_particles()# searchs the space to move th paricles to a new position
    iteration += 1# adds the iteration to the intzalized 1 to start the ieration

print("The best solution is: ", search_space.gbest_position, " for number of iterations: ", iteration)# prints out the best solution to the user

