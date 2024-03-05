# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Hierarchical clustering emphasizes the gradual merging of groups with shared similarities, providing a more gradual and resilient approach. In contrast, K-means may be impacted by individual data points, particularly outliers, as it relies on their proximity to centroids."
    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Both methods have the potential to produce different outcomes in successive runs."

    # type: bool (True/False)
    answers["(c)"] = False

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "The addition of a new centroid can lead to an increased distance between the centroid and the data points. As a consequence, the Sum of Squared Residuals (SSE) may witness an increment."
    # type: bool (True/False)
    answers["(d)"] = True

    # type: explanatory string (at least four words)
    answers["(d) explain"] = "This occurs because the split is intended to generate two sub-clusters that could be more homogeneous, thereby bringing data points closer to their respective centroids. Consequently, the total sum of squared distances within each sub-cluster (SSE) might decrease, resulting in a reduced SSE for the entire clustering solution."   
    # type: bool (True/False)
    answers["(e)"] = True

    # type: explanatory string (at least four words)
    answers["(e) explain"] = "In K-means clustering, the goal is to minimize the Sum of Squared Errors (SSE), representing the total distance between data points. The reduction in SSE indicates that the data points are moving closer to their respective cluster centroids."

    # type: bool (True/False)
    answers["(f)"] = False

    # type: explanatory string (at least four words)
    answers["(f) explain"] = "When performing K-means clustering on a dataset, an increase in SSB corresponds to an increase in separation.."

    # type: bool (True/False)
    answers["(g)"] = True

    # type: explanatory string (at least four words)
    answers["(g) explain"] = "Enhancing cohesion (by reducing SSE) aims to make data points within a cluster more similar. Yet, reducing SSE doesn't guarantee an enhancement in separation (larger SSB). It's plausible to have compact clusters (low SSE) without achieving well-separated clusters (large SSB)."
    # type: bool (True/False)
    answers["(h)"] = False

    # type: explanatory string (at least four words)
    answers["(h) explain"] = "SSE + BSS is constant because it equals TSS, but SSE and BSS individually are not constant and can change based on how well the data is clustered."


    # type: bool (True/False)
    answers["(i)"] = False

    # type: explanatory string (at least four words)
    answers["(i) explain"] = "Enhancing cohesion (by decreasing SSE) aims to make data points within a cluster more similar to each other; however, it does not automatically indicate an enhancement in separation (larger SSB)."

    return answers




# -----------------------------------------------------------
def question2():
    answers = {}

    # type: bool (True/False)
    answers["(a)"] = True

    # type: explanatory string (at least four words)
    answers["(a) explain"] = " Following the conclusion of the k-means algorithm, each shaded circle will be linked to a singular cluster centroid situated at its center."
    
    # type: bool (True/False)
    answers["(b)"] = False

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Upon completing the k-means algorithm, some clusters within the final two may include points from both shaded regions."

    # type: bool (True/False)
    answers["(c)"] = True

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "Upon completion of the k-means algorithm, the final k-means clustering includes a cluster that is empty."

    return answers




# -----------------------------------------------------------
def question3():
    answers = {}

    # type: a string that evaluates to a float
    answers["(a) SSE"] = '4*R^2'

    # type: a string that evaluates to a float
    answers["(b) SSE"] = '4*squart(a^2+b^2)'

    # type: a string that evaluates to a float
    answers["(c) SSE"] = '10*R^2'

    return answers




# -----------------------------------------------------------
def question4():
    answers = {}

    # type: int
    answers["(a) Circle (a)"] = 1

    # type: int
    answers["(a) Circle (b)"] = 1

    # type: int
    answers["(a) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "optimal clusturing will happen"

    # type: int
    answers["(b) Circle (a)"] = 1

    # type: int
    answers["(b) Circle (b)"] = 1

    # type: int
    answers["(b) Circle (c)"] = 1

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Considering the similar distances between circles A and B, as well as between circles B and C, it is anticipated that each centroid will converge within its initial circle."
    # type: int
    answers["(c) Circle (a)"] = 1

    # type: int
    answers["(c) Circle (b)"] = 0

    # type: int
    answers["(c) Circle (c)"] = 2

    # type: explanatory string (at least four words)
    answers["(c) explain"] = "To achieve optimal clustering, this distribution guarantees that each centroid is nearest to the cluster to which it initially belonged."

    return answers




# -----------------------------------------------------------
def question5():
    answers = {}

    # type: set
    answers["(a)"] = {"Group A","Group B"}

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "The shortest path separating the top left point in Group A from the top right point in Group B is the distance between them."

    # type: set
    answers["(b)"] = {'Group A','Group C'}

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "The longest distance between the bottom left point in Group C and the bottom right point in Group A is the separation between them."

    return answers




# -----------------------------------------------------------
def question6():
    answers = {}

    # type: set
    answers["(a) core"] = {'E','B','F','G','C','L','M','I'}

    # type: set
    answers["(a) boundary"] = {'D','G'}

    # type: set
    answers["(a) noise"] = {'A','H'}

    # type: set
    answers["(b) cluster 1"] = {'B','C','E','F','G','D'}

    # type: set
    answers["(b) cluster 2"] = {'I','J','L','M'}

    # type: set
    answers["(b) cluster 3"] = set()

    # type: set
    answers["(b) cluster 4"] = set()

    # type: set
    answers["(c)-a core"] = {'B','C','D','E','F','G','I','J','L','M'}

    # type: set
    answers["(c)-a boundary"] = {'A','H'}

    # type: set
    answers["(c)-a noise"] = set()

    # type: set
    answers["(c)-b cluster 1"] = {'A','B','C','D','E','F','G','H','I','J','L','M'}

    # type: set
    answers["(c)-b cluster 2"] = {'A'}

    # type: set
    answers["(c)-b cluster 3"] = set()

    # type: set
    answers["(c)-b cluster 4"] = set()

    return answers




# -----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    answers["(a)"] = "cluster 4"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "Cluster 4 shows the highest entropy, indicating a varied composition of land cover types within it."

    # type: string
    answers["(b)"] = "cluster 1"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "Cluster 1 showcases the lowest entropy, signifying a more uniform assortment of land cover categories within it."

    return answers




# -----------------------------------------------------------
def question8():
    answers = {}

    # type: string
    answers["(a) Matrix 1"] = "Dataset-z"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 1"] = "The presence of the color blue indicates short distances, signifying clear and well-separated clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 1"] = "Diverse color patterns suggest an alternative configuration of clusters."

    # type: string
    answers["(a) Matrix 2"] = "Dataset-x"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 2"] = "The blue color represents short distances, indicating clear and well-separated clusters."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 2"] = "All other colors indicate long distances, suggesting distinct boundaries between clusters."

    # type: string
    answers["(a) Matrix 3"] = "Dataset-y"

    # type: explanatory string (at least four words)
    answers["(a) explain diag entries, Matrix 3"] = "The diagonal entry corresponds to the distance of a point from itself."

    # type: explanatory string (at least four words)
    answers["(a) explain non-diag entries, Matrix 3"] = "Specific regions in green and yellow imply clusters that either overlap or are not distinctly defined.."

    # type: string
    answers["(b) Row 1"] = "Cluster-a"

    # type: string
    answers["(b) Row 2"] = "Cluster-b"

    # type: string
    answers["(b) Row 3"] = "Cluster-c"

    # type: string
    answers["(b) Row 4"] = "Cluster-d"

    # type: explanatory string (at least four words)
    answers["(b) Row 1 explain"] = "The clarity of the diagonal entry is diminished, suggesting that the cohesiveness of the cluster is compromised. Furthermore, the variation in color among the off-diagonal entries signifies that the distances to other clusters are distinct, with the proximity to cluster B being the nearest, followed by cluster C, and cluster A being the most distant."

    # type: explanatory string (at least four words)
    answers["(b) Row 2 explain"] = "The enhanced clarity of the diagonal entry suggests a higher degree of cohesiveness within the cluster. Additionally, the uniformity in color of two-thirds of the off-diagonal entries indicates proximity to two other clusters (A and C), despite the less distinct appearance of the off-diagonal entry signifying distance from cluster A. This configuration reveals that the cluster is most distanced from another cluster, designated as D."

    # type: explanatory string (at least four words)
    answers["(b) Row 3 explain"] = "The explanation is same as to row 2"

    # type: explanatory string (at least four words)
    answers["(b) Row 4 explain"] = "The Explanation is same as row 1 in inverted order"

    return answers




# -----------------------------------------------------------
def question9():
    answers = {}

    # type: list
    answers["(a)"] = ['hierarchical', 'overlapping', 'partial']

    # type: list
    answers["(b)"] = ['partitional', 'exclusive', 'complete']

    # type: list
    answers["(c)"] = ['partitional', 'fuzzy', 'complete']

    # type: list
    answers["(d)"] = ['hierarchical','overlapping', 'partial']

    # type: list
    answers["(e)"] = ['partitional', 'exclusive', 'complete']

    # type: explanatory string (at least four words)
    answers["(e) explain"] = ""

    return answers




# -----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    answers["(a) Figure (a)"] = "No"

    # type: string
    answers["(a) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(a) explain"] = "In Figure B, the efficacy of DBSCAN in recognizing facial representations is rooted in its capacity to assess the spatial density of the data points."

    # type: string
    answers["(b) Figure (a)"] = "No"

    # type: string
    answers["(b) Figure (b)"] = "Yes"

    # type: explanatory string (at least four words)
    answers["(b) explain"] = "It is a method that clusters similar data points to recognize patterns in a dataset. Concerning facial characteristics, k-means can be employed to identify patterns based on dimensions, positions, and shapes."

    # type: string
    answers["(c)"] = "DBSCAN"

    return answers

# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()
    print('end code')

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
