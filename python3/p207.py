class Solution:

    @staticmethod
    def take_course(numCourses: int, depends_on:Dict[int, int]) -> int:
        """
        take all the courses with no pre-requisites then update the
        depends_on dict to account for the fact we took the course,
        so it's no longer tracked as a pre-req for anything else
        """
        no_prereq = [k for k,v in depends_on.items() if not v]

        for n_p in no_prereq:
            for v in depends_on.values():
                v.discard(n_p)
            del depends_on[n_p]

        return numCourses - len(no_prereq)


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        depends_on = {}

        if not prerequisites:
            return True

        # build dict where
        #  key: course ID
        #  value: set of courses that must be taken first
        # if no dependencies, use empty set
        for p in prerequisites:
            if p[0] not in depends_on:
                depends_on[p[0]] = set()
            if p[1] not in depends_on:
                depends_on[p[1]] = set()

            depends_on[p[0]].add(p[1])

        while numCourses > 0:
            prior_num_courses = numCourses
            numCourses = Solution.take_course(numCourses, depends_on)
            if prior_num_courses == numCourses:
                return False

            if not depends_on:
                return True
        return True

