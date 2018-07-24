/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  android.text.TextUtils
 *  com.meituan.robust.utils.EnhancedRobustUtils
 *  com.meituan.sample.robusttest.d
 */
package com.meituan.robust.patch;

import android.text.TextUtils;
import com.meituan.robust.utils.EnhancedRobustUtils;
import com.meituan.sample.robusttest.d;

public class ImageQualityUtilInLinePatch {
    d originClass;

    public ImageQualityUtilInLinePatch(Object object) {
        this.originClass = (d)object;
    }

    public static String getLargeUrl(String string) {
        new ImageQualityUtilInLinePatch(null);
        return ImageQualityUtilInLinePatch.getQualityUrl(string, "/440.267/");
    }

    /*
     * Enabled force condition propagation
     * Lifted jumps to return sites
     */
    public static String getQualityUrl(String string, String string2) {
        if (!TextUtils.isEmpty((CharSequence)string)) return d.b((String)((String)EnhancedRobustUtils.invokeReflectMethod((String)"replace", (Object)string, (Object[])new Object[]{"/w.h/", string2}, (Class[])new Class[]{CharSequence.class, CharSequence.class}, String.class)));
        return "";
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
}

