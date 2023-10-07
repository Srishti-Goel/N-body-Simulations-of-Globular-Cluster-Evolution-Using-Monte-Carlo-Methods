import numpy as np
import matplotlib.pyplot as plt

# Comptuational constants
G = 6.67e-11 # Gravitational constant
N = 300 # No. of normal-matter particles
MASS_INITIALLY = 2e30 # Initiating at 1 solar mass

LENGTH_SCALE = 1e15
N_SWEEPS = 1 # No. of sweeps
RELAXATION_CONST = 1e12
COLLISION_CONST = 1e-35
ENCOUNTER_PROB_CONST = 1e-19
ELASTICITY_OF_ENCOUNTER = 1
sigma_2 = 1
MAX_R = 100 * LENGTH_SCALE # Maximum dimensions of the cluster observed


# Initialize the universe
particles = np.random.uniform(0, 100, size=(N, 9)) # Radius, velocity_x, velocity_y, velocity_z, mass, energy, angular_momentum, theta, phi
particles[:, 4] = MASS_INITIALLY
particles[:, 0:4] *= LENGTH_SCALE
particles[:, 5] = .5 * MASS_INITIALLY * np.linalg.norm(particles[:, 0:4], axis=1) 
particles[:, 7:9] *= LENGTH_SCALE


# Sorting them based on radius: (increasing order)
particles = particles[particles[:, 0].argsort()]

# print(particles[:, 5])

potential = np.zeros(shape=(N))
mass_loss_due_to_stellar_evolution = 1
previous_time_step = 1

# For each time step:
for time in range(N_SWEEPS):

    # Calculate potential
    M_n = np.sum(particles[:, 4])
    prev_pot = 0
    potential[-1] = - G * particles[-1, 4] / particles[-1, 0]

    for k in range(N-2, -1, -1):
        potential[k] = prev_pot - (G * particles[k, 4] * ((1/particles[k, 0]) - (1/particles[k+1, 0])))
        prev_pot = potential[k]
    
    particles[:, 5] = potential*particles[:, 4] + .5 * particles[:, 4] * np.linalg.norm(particles[:, 0:4], axis=1)**2 # Total energy is the U + KE

    # print(potential[-10:])
    # plt.plot(particles[:, 0], potential)
    # plt.plot(particles[:, 0], particles[:, 5])
    # plt.show()

    # Calculate time-step
    # Relaxation times:
    t_rel_min = 1e10
    for k in range(N):
        vrels = (particles[:, 1:4] - particles[k, 1:4])**2
        vrels_mag = np.sqrt(np.sum(vrels, axis = 1))
        vrels_avg = np.mean(vrels_mag)

        masses_squared = (particles[:, 4] + particles[k, 4])**2
        masses_rms = np.mean(masses_squared)

        temp = RELAXATION_CONST * vrels_avg ** 3 / masses_rms

        t_rel_min = min(t_rel_min, temp)

    # Collision times:
    central_velocity_dispersion = 0 #TODO
    average_stellar_mass_in_core = np.mean(particles[:300, 4])
    central_density = average_stellar_mass_in_core * 300 / (4 * np.pi * particles[299, 0]**3 / 3)

    radius_ms = np.mean(particles[:300, 0]**2)
    mass_radius_mean = np.mean(particles[:300, 0] * particles[:300, 4])
    # print(radius_ms, mass_radius_mean)

    t_coll = 1/(COLLISION_CONST * radius_ms * (1 + ((G * mass_radius_mean) / (2 * sigma_2 * radius_ms))))

    t_stellar_evolution = 0.001 * M_n * previous_time_step / mass_loss_due_to_stellar_evolution

    previous_time_step = new_time_step = min(t_rel_min, t_coll, t_stellar_evolution)

    # print(t_coll, t_stellar_evolution, t_rel_min)


    # Collision:
    collision_count = 0
    for k in range(N):
        if k >= N:
            break
        for k2 in range(N):
            if k == k2:
                continue
            if k2 >= N:
                break
            v_rel = particles[k, 1:4] - particles[k2, 1:4]
            prob_of_encounter = ENCOUNTER_PROB_CONST * np.linalg.norm(v_rel) * new_time_step
            r = np.random.uniform(0,1)

            if r < prob_of_encounter:
                # I assume a sticky collision, and then calculate new radius of the centre of mass from there
                m1 = particles[k, 4]
                m2 = particles[k2, 4]

                v1 = particles[k, 1:4]
                v2 = particles[k2, 1:4]

                r1 = particles[k, 0]
                r2 = particles[k2, 0]

                new_vel = ((m1 * v1) + (m2 * v2)) / (m1 + m2)
                new_mass = (m1 + m2)
                new_radius = ((m1 * r1) + (m2 * r2)) / (m1 + m2)
                new_pot = 0
                for k in range(N):
                    if particles[k, 0] > new_radius:
                        new_pot = potential[max(k, 0)] * new_mass
                        break
                new_energy = new_pot + (0.5 * new_mass * np.linalg.norm(new_vel)**2)
                new_angular_momentum = new_mass * new_radius 
                
                particles[k, 0] = new_radius
                particles[k, 1:4] = new_vel
                particles[k, 4] = new_mass

                particles = np.delete(particles, k2, 0)
                potential = np.delete(potential, k2)
                
                N -= 1
                collision_count += 1
                # print(prob_of_encounter)
                break
    print(collision_count)

    # Stellar evolution
    # TODO: Calculate how much mass to remove

    # New orbits and positions

    print(particles.shape)
    # print(particles[:100, :])
    potential = potential[particles[:, 0] < MAX_R]
    particles = particles[particles[:, 0] < MAX_R, :]
    print(particles.shape)


# Sort by radial distance
