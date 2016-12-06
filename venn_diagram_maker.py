from matplotlib_venn import *
from matplotlib import pyplot as plt


A = 'A'
B = 'B'
intersect="$%s \\cap %s$" % (A, B)

A_expl = 'explanation of A'; 
B_expl = 'explanation of B';
q_A = None
q_B = None
intersect_quantity = None
completment_AB=None
total_quantity=None


def calculate_sets(q_A, intersect_quantity, q_B, complement_AB, total_quantity):

    if intersect_quantity == None:
        q_AUB = total_quantity - complement_AB 
        intersect_quantity = q_A + q_B - q_AUB
        q_A_disjoint = q_A - intersect_quantity
        q_B_disjoint = q_B - intersect_quantity

        return q_A_disjoint, intersect_quantity, q_B_disjoint, complement_AB

    else:
        q_AUB = q_A + q_B - intersect_quantity # addition rule of non-disjoint sets
        
        complement_AB = total_quantity - q_AUB

        q_A_disjoint = q_A - intersect_quantity
        q_B_disjoint = q_B - intersect_quantity

        return q_A_disjoint, intersect_quantity, q_B_disjoint, complement_AB

# test on examples p 297 - 298 in Ascehhoug matte paabygg
elevliste_sommerjobb_ferie = calculate_sets(15, None, 12, 5, 23)
print(elevliste_sommerjobb_ferie)
elevliste_xfactor_71nord = calculate_sets(12, 4, 10, None, 25)
print(elevliste_xfactor_71nord)

def draw_venn_diagram(arglist):
    #unpack arglist
    q_A_disjoint, q_intersect, q_B_disjoint, complement_AB = arglist
    v = venn2(subsets = {'10': 1, '01': 1, '11': 1}, set_labels = (A, B))
    v.get_patch_by_id('10').set_alpha(0.5)
    v.get_patch_by_id('10').set_color('blue')
    v.get_patch_by_id('01').set_alpha(0.3)
    v.get_patch_by_id('01').set_color('yellow')
    v.get_patch_by_id('11').set_alpha(0.5)
    v.get_patch_by_id('11').set_color('green')
    v.get_label_by_id('10').set_text(q_A_disjoint)
    v.get_label_by_id('01').set_text(q_intersect)
    v.get_label_by_id('11').set_text(q_B_disjoint)
    v.get_label_by_id(A).set_text('')
    v.get_label_by_id(B).set_text('')
    v.get_label_by_id(A).set_size(20)
    v.get_label_by_id(B).set_size(20)
    plt.annotate(A, xy = v.get_label_by_id('10').get_position(), xytext = (-30,120), size = 'xx-large',
                ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.0', fc = 'lime', alpha = 0.0),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = 0.5', color = 'gray'))

    plt.annotate(B, xy = v.get_label_by_id('01').get_position(), xytext = (30,120), size = 'xx-large',
                ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.0', fc = 'lime', alpha = 0.0),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3, rad = -0.5',color = 'gray'))

    plt.annotate(intersect, xy = v.get_label_by_id('11').get_position(), xytext = (0,-180), size = 'xx-large',
                ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.0', fc = 'lime', alpha = 0.0),
                arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad = 0',color = 'gray'))


    plt.annotate(complement_AB, xy = v.get_label_by_id('11').get_position(), xytext = (180,-190), size = 'xx-large',
                ha = 'center', textcoords = 'offset points', bbox = dict(boxstyle = 'round, pad = 0.0', fc = 'lime', alpha = 0.0))

    plt.show()

draw_venn_diagram(elevliste_sommerjobb_ferie)



