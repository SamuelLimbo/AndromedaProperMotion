import gala as gc
import astropy.units as u
from astropy.coordinates import SkyCoord
import astropy.coordinates as coord

def reflex_correct(coords, galactocentric_frame=None):
    #___ Description_____________________________________________________________________________________
    #Arguments:: the Astropy coordinate object with position and velocity information. The second is an
    #           optional argument that allows to change the properties of the galactocentric frame
    #Returns:: The coordinates in the same frame as input, but with solar motion removed
    #____________________________________________________________________________________________________

    c = coord.SkyCoord(coords)

    # If not specified, use the Astropy default Galactocentric frame
    if galactocentric_frame is None:
        galactocentric_frame = coord.Galactocentric()

    v_sun = galactocentric_frame.galcen_v_sun

    observed = c.transform_to(galactocentric_frame)
    rep = observed.cartesian.without_differentials()
    rep = rep.with_differentials(observed.cartesian.differentials["s"] + v_sun)
    fr = galactocentric_frame.realize_frame(rep).transform_to(c.frame)
    return coord.SkyCoord(fr)

#We just have to enter the position of the object and we can easily derive it's
#proper motion with respect to us
c = coord.SkyCoord(ra=10.68*u.deg,
                    dec=41.27*u.deg,
                    distance=780000*u.pc,
                    pm_ra_cosdec=0*u.mas/u.yr,
                    pm_dec=0*u.mas/u.yr,
                    radial_velocity=203*u.km/u.s)

vsun = coord.CartesianDifferential([10.6, 247, 7.6]*u.km/u.s) #customise the velocity of the Sun
gc_frame = coord.Galactocentric(galcen_v_sun=vsun, z_sun=0*u.pc)
A = reflex_correct(c, gc_frame)

print("The motion along ra is:", A.pm_ra_cosdec.value*1000, "µas/yr")
print("The motion along dec is:", A.pm_dec.value*1000, "µas/yr")
