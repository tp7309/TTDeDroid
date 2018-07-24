/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  android.os.Bundle
 *  com.meituan.robust.utils.EnhancedRobustUtils
 *  com.meituan.sample.SecondActivity
 *  com.meituan.sample.robusttest.o
 *  com.meituan.sample.robusttest.other.a
 */
package com.meituan.robust.patch;

import android.os.Bundle;
import com.meituan.robust.utils.EnhancedRobustUtils;
import com.meituan.sample.SecondActivity;
import com.meituan.sample.robusttest.o;
import com.meituan.sample.robusttest.other.a;

public class SecondActivityInLinePatch {
    SecondActivity originClass;

    public SecondActivityInLinePatch(Object object) {
        this.originClass = (SecondActivity)object;
    }

    public static String[] methodWithArrayParameters(String[] arrstring) {
        return arrstring;
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

    public o getTextI2(String string) {
        new Bundle().get("asdas");
        return (o)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.robusttest.o", (Object[])this.getRealParameter(new Object[]{(a)EnhancedRobustUtils.invokeReflectConstruct((String)"com.meituan.sample.robusttest.other.a", (Object[])this.getRealParameter(new Object[]{new Boolean(false)}), (Class[])new Class[]{Boolean.TYPE})}), (Class[])new Class[]{a.class});
    }
}

