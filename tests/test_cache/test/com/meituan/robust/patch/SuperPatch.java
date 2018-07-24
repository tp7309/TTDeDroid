/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  com.meituan.robust.utils.EnhancedRobustUtils
 *  com.meituan.sample.robusttest.CallBack
 *  com.meituan.sample.robusttest.other.a
 *  com.meituan.sample.robusttest.p
 */
package com.meituan.robust.patch;

import com.meituan.robust.utils.EnhancedRobustUtils;
import com.meituan.sample.robusttest.CallBack;
import com.meituan.sample.robusttest.other.a;
import com.meituan.sample.robusttest.p;

public class SuperPatch {
    p originClass;

    public SuperPatch(Object object) {
        this.originClass = (p)object;
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
        int n2 = 0;
        while (n2 < arrobject.length) {
            arrobject2[n2] = arrobject[n2] == this ? this.originClass : arrobject[n2];
            ++n2;
        }
        return arrobject2;
    }

    /*
     * Enabled aggressive block sorting
     */
    public String getText1(int n2, Long object, Integer n3) {
        object = this instanceof SuperPatch ? this.originClass : this;
        n3 = (a)EnhancedRobustUtils.getFieldValue((String)"j", (Object)object, p.class);
        object = n3;
        if (n3 == this) {
            object = ((SuperPatch)n3).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"f", (Object)object, (Object[])new Object[0], null, a.class);
        object = this instanceof SuperPatch ? this.originClass : this;
        n3 = (a)EnhancedRobustUtils.getFieldValue((String)"j", (Object)object, p.class);
        object = n3;
        if (n3 == this) {
            object = ((SuperPatch)n3).originClass;
        }
        EnhancedRobustUtils.invokeReflectMethod((String)"callBack", (Object)object, (Object[])new Object[0], null, CallBack.class);
        object = (p)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.robusttest.p", (Object[])new Object[0], null);
        throw new ArithmeticException("divide by zero");
    }
}

