/*
 * Decompiled with CFR 0_132.
 * 
 * Could not load the following classes:
 *  com.meituan.robust.PatchedClassInfo
 *  com.meituan.robust.PatchesInfo
 *  com.meituan.robust.utils.EnhancedRobustUtils
 */
package com.meituan.robust.patch;

import com.meituan.robust.PatchedClassInfo;
import com.meituan.robust.PatchesInfo;
import com.meituan.robust.utils.EnhancedRobustUtils;
import java.util.ArrayList;
import java.util.List;

public class PatchesInfoImpl
implements PatchesInfo {
    public List getPatchedClassesInfo() {
        ArrayList<PatchedClassInfo> arrayList = new ArrayList<PatchedClassInfo>();
        arrayList.add(new PatchedClassInfo("com.meituan.sample.robusttest.l", "com.meituan.robust.patch.SampleClassPatchControl"));
        arrayList.add(new PatchedClassInfo("com.meituan.sample.robusttest.p", "com.meituan.robust.patch.SuperPatchControl"));
        arrayList.add(new PatchedClassInfo("com.meituan.sample.SecondActivity", "com.meituan.robust.patch.SecondActivityPatchControl"));
        EnhancedRobustUtils.isThrowable = false;
        return arrayList;
    }
}

