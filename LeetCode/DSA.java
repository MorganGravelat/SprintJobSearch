//Median of Two Sorted Arrays
class Solution {

    // The input arrays (longer one first)
    private int[] run1, run2;

    // Number of elements before the median of the merged array
    private int numToTrim;
    // Current position in each array as elements are removed from the front
    private int pos1, pos2;

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        final boolean swap = nums2.length > nums1.length;
        this.run1 = swap ? nums2 : nums1;
        this.run2 = swap ? nums1 : nums2;
        this.pos1 = 0;
        this.pos2 = 0;

        // We'll be trimming everything before the median. Determine how many items to trim
        final int len = run1.length + run2.length;
        final boolean hasMid = len % 2 == 1;
        numToTrim = len / 2 - (hasMid ? 0 : 1);

        // If numToTrim is c more than run2 length, trim c from run1 as at least c must come from run1
        if (numToTrim > run2.length) {
            pos1 = numToTrim - run2.length;
            numToTrim -= pos1;
        }

        // Each iteration of this loop removes half the remaining excess, ensuring log(n) complexity
        while (numToTrim > 1) {
            trimHead();
        }

        // The last element may have to be trimmed manually, as trimHead requires at least 2
        if (numToTrim == 1) {
            trim1();
        }

        // If there was an exact middle element, get it and return it
        int mid1 = trim1();
        if(hasMid) return mid1;

        // Otherwise get the next element as well and average them
        int mid2 = trim1();
        return ((double) mid1 + mid2) / 2;
    }

    private void trimHead() {
        // We'll attempt to remove half numToTrim from each array. Split into equal parts (may differ by 1)
        int trim1 = numToTrim / 2;
        int trim2 = numToTrim - trim1;

        // Check the value of the last element we're attempting to remove in each array
        int val1 = run1[pos1 + trim1 - 1];
        int val2 = run2[pos2 + trim2 - 1];

        // Whichever is lower, trim it and everything before it. If equal, both arrays will be trimmed
        if (val1 <= val2) {
            pos1 += trim1;
            numToTrim -= trim1;
        }
        if (val2 <= val1) {
            pos2 += trim2;
            numToTrim -= trim2;
        }
    }

    // Find, remove, and return the next item in the merged array
    int trim1() {
        if (pos1 >= run1.length) return run2[pos2++];
        if (pos2 >= run2.length) return run1[pos1++];
        return run1[pos1] <= run2[pos2] ? run1[pos1++] : run2[pos2++];
    }
}
