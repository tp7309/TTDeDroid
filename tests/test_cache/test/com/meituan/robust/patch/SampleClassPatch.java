/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  com.meituan.robust.utils.EnhancedRobustUtils
 *  com.meituan.sample.robusttest.l
 *  com.meituan.sample.robusttest.m
 *  com.meituan.sample.robusttest.n
 */
package com.meituan.robust.patch;

import com.meituan.robust.utils.EnhancedRobustUtils;
import com.meituan.sample.robusttest.l;
import com.meituan.sample.robusttest.m;
import com.meituan.sample.robusttest.n;
import java.io.PrintStream;

public class SampleClassPatch {
    l originClass;

    public SampleClassPatch(Object object) {
        this.originClass = (l)object;
    }

    /*
     * Enabled aggressive block sorting
     */
    public Object[] getRealParameter(Object[] arrobject) {
        Object[] arrobject2 = arrobject;
        if (arrobject == null) return arrobject2;
        if (arrobject.length < 1) {
            return arrobject;
        }
        arrobject2 = new Object[arrobject.length];
        int n = 0;
        while (n < arrobject.length) {
            arrobject2[n] = arrobject[n] == this ? this.originClass : arrobject[n];
            ++n;
        }
        return arrobject2;
    }

    public int multiple(int n2) {
        Object object;
        Object object2 = object = (m)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.robusttest.m", (Object[])this.getRealParameter(new Object[]{this}), (Class[])new Class[]{l.class});
        if (object == this) {
            object2 = ((SampleClassPatch)object).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"a", (Object)object2, (Object[])this.getRealParameter(new Object[]{"asdad"}), (Class[])new Class[]{String.class}, n.class);
        n2 = (Integer)EnhancedRobustUtils.invokeReflectMethod((String)"b", (Object)this.originClass, (Object[])this.getRealParameter(new Object[]{new Integer(n2)}), (Class[])new Class[]{Integer.TYPE}, l.class);
        object2 = object = System.out;
        if (object == this) {
            object2 = ((SampleClassPatch)object).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"print", (Object)object2, (Object[])this.getRealParameter(new Object[]{"hellow world 1"}), (Class[])new Class[]{String.class}, PrintStream.class);
        object2 = this;
        if (this instanceof SampleClassPatch) {
            object2 = this.originClass;
        }
        return (Integer)EnhancedRobustUtils.getFieldValue((String)"d", (Object)object2, l.class) * n2;
    }
}

